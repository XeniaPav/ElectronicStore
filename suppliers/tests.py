from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from suppliers.models import Supplier
from users.models import User


class SupplierTestCase(APITestCase):
    """Класс тестирования CRUD поставщика"""

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.suppliers = None

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.client.force_authenticate(user=self.user)
        self.supplier = Supplier.objects.create(
            name="завод",
            email="test@mail.ru",
            country="РФ",
            city="Москва",
            street="Пушкина",
            house_number="1",
            level="1",
        )

    def test_supplier_retrieve(self):
        """Просмотр"""
        url = reverse("suppliers:retrieve", args=(self.supplier.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.supplier.name)

    def test_supplier_create(self):
        """Создание"""
        url = reverse("suppliers:create")
        data = {
            "name": "test",
            "email": "test@test.com",
        }
        data1 = {
            "name": "test",
        }
        response = self.client.post(url, data)
        response1 = self.client.post(url, data1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.all().count(), 2)
        self.assertEqual(response1.status_code, status.HTTP_400_BAD_REQUEST)

    def test_supplier_update(self):
        """Редактирование"""
        url = reverse("suppliers:update", args=(self.supplier.pk,))
        data = {"name": "Завод 1"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supplier_list(self):
        """Просмотр списка"""
        url = reverse("suppliers:list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_supplier_delete(self):
        """Удаление"""
        url = reverse("suppliers:delete", args=(self.supplier.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Supplier.objects.all().count(), 0)
