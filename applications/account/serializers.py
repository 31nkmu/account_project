from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')
        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадаюют!')
        return attrs

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        user.is_active = True
        # TODO: send message
        return User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    @staticmethod
    def validate_email(email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь не зарегистрирован')
        return email

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(username=email,
                            password=password)
        if not user:
            raise serializers.ValidationError('Неверный email или пароль')
        attrs['user'] = user
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, max_length=128, min_length=6)
    new_password_confirm = serializers.CharField(required=True, min_length=6, max_length=128)

    def validate(self, attrs):
        ps1 = attrs.get('new_password')
        ps2 = attrs.get('new_password_confirm')
        if ps1 != ps2:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def validate_old_password(self, p):
        req = self.context.get('request')
        user = req.user
        if not user.check_password(p):
            raise serializers.ValidationError('Неверный пароль!')
        return p

    def set_new_password(self):
        user = self.context.get('request').user
        password = self.validated_data.get('new_password')
        # user.password = make_password(password)
        user.set_password(password)
        user.save()

