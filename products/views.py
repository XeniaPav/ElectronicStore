from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductSerializer
from suppliers.paginators import CustomPagination
from users.permissions import IsActive


class ProductViewSet(ModelViewSet):
    """CRUD для продуктов"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
    pagination_class = CustomPagination
