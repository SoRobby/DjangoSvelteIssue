from apps.supplier.models import UserRole


def is_user_linked_to_supplier(user, supplier):
    return UserRole.objects.filter(user=user, role__supplier=supplier).exists()
