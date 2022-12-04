from rest_framework import serializers

from applications.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        product = Product.objects.create(owner=user, **validated_data)
        return product
        # product = super(ProductSerializer, self).create(validated_data)
        # product['owner'] = user
        # return product
