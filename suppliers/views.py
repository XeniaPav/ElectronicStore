from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from suppliers.models import Supplier
from suppliers.paginators import CustomPagination
from suppliers.serializers import SupplierSerializer
from users.permissions import IsActive


class SupplierCreateAPIView(CreateAPIView):
    """CRUD для создания поставщика"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActive]


class SupplierListAPIView(ListAPIView):
    """CRUD для просмостра списка поставщиков"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActive]
    filterset_fields = ("country",)
    pagination_class = CustomPagination


class SupplierRetrieveAPIView(RetrieveAPIView):
    """CRUD для просмостра  поставщика"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActive]


class SupplierUpdateAPIView(UpdateAPIView):
    """CRUD для обновления списка поставщиков"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActive]

    def perform_update(self, serializer):
        if "debts" in serializer.validated_data:
            serializer.validated_data.pop("debts")
            raise Exception("Вы не можете менять поле задолженности")
        super().perform_update(serializer)


class SupplierDestroyAPIView(DestroyAPIView):
    """CRUD для удаления списка поставщиков"""

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActive]
