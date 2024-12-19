from django.urls import path

from suppliers.apps import SuppliersConfig
from suppliers.views import (
    SupplierCreateAPIView,
    SupplierDestroyAPIView,
    SupplierListAPIView,
    SupplierRetrieveAPIView,
    SupplierUpdateAPIView,
)

app_name = SuppliersConfig.name
urlpatterns = [
    path("", SupplierListAPIView.as_view(), name="list"),
    path("create/", SupplierCreateAPIView.as_view(), name="create"),
    path("<int:pk>/", SupplierRetrieveAPIView.as_view(), name="retrieve"),
    path("<int:pk>/update/", SupplierUpdateAPIView.as_view(), name="update"),
    path("<int:pk>/delete/", SupplierDestroyAPIView.as_view(), name="delete"),
]
