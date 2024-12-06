from django.db import models

from apps.core.custom_fields import KeyField
from apps.core.models import SoftDeletionWithUserModel, UserTrackingModel
from config import settings
from .supplier import Supplier


class Permission(UserTrackingModel, SoftDeletionWithUserModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True,
                               verbose_name='Parent', help_text='Parent permission')

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the permission')

    code = KeyField(verbose_name='Code', help_text='Code of the permission')

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the permission')

    class Meta:
        ordering = ['code']
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissions'
        indexes = [
            models.Index(fields=['code']),
        ]

    def __str__(self):
        return f'{self.code} - {self.name}'


#
class Role(UserTrackingModel, SoftDeletionWithUserModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_roles',
                                 verbose_name='Supplier', help_text='Supplier of the role')

    permission = models.ManyToManyField(Permission, related_name='permission_roles', verbose_name='Permissions',
                                        help_text='Permissions of the role')

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the role')

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the role')

    class Meta:
        ordering = ['supplier', 'name']
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return f'{self.supplier.name} - {self.name}'


class UserRole(UserTrackingModel, SoftDeletionWithUserModel):
    # TODO - May want to make this a OneToOneField to enforce only one role per user
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_roles',
                             verbose_name='User', help_text='User of the user role')

    # supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='user_roles', verbose_name='Supplier',
    #                              help_text='Supplier of the user role')

    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='user_roles', verbose_name='Role',
                             help_text='Role of the user')

    class Meta:
        ordering = ['user']
        unique_together = ('user', 'role')
        verbose_name = 'User role'
        verbose_name_plural = 'User roles'

    def __str__(self):
        return f'{self.user.username} - {self.role.name}'

    # TODO - Before saving make sure that the user is part of that particular supplier.
