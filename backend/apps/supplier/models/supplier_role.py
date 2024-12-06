from django.db import models

from apps.core.models import UserTrackingModel
from config import settings
from .supplier import Supplier


class SupplierRole(UserTrackingModel):
    class RoleChoices(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        STAFF = 'staff', 'Staff'

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='roles', verbose_name='Supplier',
                                 help_text='Supplier of the role')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='supplier_roles',
                             verbose_name='User', help_text='User of the role')

    role = models.CharField(max_length=16, choices=RoleChoices.choices, verbose_name='Role',
                            help_text='Role of the user')

    class Meta:
        ordering = ['user']
        unique_together = ('supplier', 'user')
        verbose_name = 'Supplier role'
        verbose_name_plural = 'Supplier roles'

    def __str__(self) -> str:
        return f'{self.user.username} - {self.supplier.name} (Role={self.role})'
