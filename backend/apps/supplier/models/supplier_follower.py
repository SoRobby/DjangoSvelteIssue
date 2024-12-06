from django.db import models

from apps.core.models import BaseModel
from config import settings
from .supplier import Supplier


class SupplierFollower(BaseModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='followers', verbose_name='Supplier',
                                 help_text='Supplier of the follower')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='supplier_followers',
                             verbose_name='User', help_text='User that is following the supplier')

    class Meta:
        ordering = ['user']
        unique_together = ('supplier', 'user')
        verbose_name = 'Supplier follower'
        verbose_name_plural = 'Supplier followers'

    def __str__(self) -> str:
        return f'{self.user.username} - {self.supplier.name}'
