from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериалайзер для продуктов"""

    class Meta:
        model = Product
        fields = "__all__"
