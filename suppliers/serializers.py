from rest_framework import serializers

from suppliers.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """Сериалайзер для поставщика"""

    class Meta:
        model = Supplier
        fields = "__all__"
