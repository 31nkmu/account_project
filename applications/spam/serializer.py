from rest_framework import serializers

from applications.spam.models import Spam


class SpamSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = Spam
        fields = '__all__'

    def create(self, validated_data):
        email = self.context.get('request').user
        spam = Spam.objects.create(email=email)
        return spam















