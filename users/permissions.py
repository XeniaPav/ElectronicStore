from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """Проверка на активного пользователя"""
    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
