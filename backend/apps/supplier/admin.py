from apps.core.utils import AdminExportMixin
from django.contrib import admin

from .models import (
    Permission,
    Role,
    Supplier,
    SupplierAlternativeName,
    SupplierContact,
    SupplierFile,
    SupplierFileVersion,
    SupplierFollower,
    SupplierJob,
    SupplierLocation,
    SupplierRole,
    SupplierTag,
    UserRole,
)


# Admin objects
@admin.register(SupplierTag)
class SupplierTagAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['name', 'slug', 'date_created', 'date_modified']

    search_fields = ['name', 'description']

    autocomplete_fields = []

    prepopulated_fields = {'slug': ['name']}

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Tag', {
            'fields': ['name', 'slug', 'description'],
            'description': 'Fields related to the property tag'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['name', 'slug', 'date_created', 'date_modified']

    list_filter = ['status', 'is_deleted']

    filter_horizontal = ()

    search_fields = ['name', 'legal_name', 'slug', 'acronym']

    autocomplete_fields = ['acquired_by', 'tags', 'blocked_countries', 'created_by', 'modified_by', 'deleted_by']

    prepopulated_fields = {'slug': ['name', ]}

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Supplier', {
            'fields': ['name', 'legal_name', 'slug', 'acronym', 'tagline', 'description', 'website'],
            'description': 'Fields related to the property tag'
        }),
        ('Logo', {
            'fields': ['logo_raw', 'logo', 'logo_thumbnail'],
            'description': 'Only upload a logo to the logo_raw field, the "logo" and "logo_thumbnail" fields are will\
            automatically be populated after the logo is uploaded and processed'
        }),
        ('Details', {
            'fields': ['number_of_employees', 'year_founded', 'tags', 'is_premium', 'status', 'acquired_by'],
            'description': 'Fields related to the property tag'
        }),
        ('Social media links', {
            'fields': ['facebook_link', 'instagram_link', 'linkedin_link', 'youtube_link', 'x_link'],
            'description': 'Fields related to the property tag'
        }),
        ('Settings', {
            'fields': ['blocked_countries'],
            'description': 'Fields related to the property tag'
        }),
        ('SEO meta tags', {
            'fields': ['meta_title', 'meta_description', 'meta_keywords'],
            'description': 'Fields related to the property tag'
        }),
        ('Admin properties', {
            'fields': ['is_hidden', 'is_blacklisted', 'admin_notes'],
            'description': 'Settings and flags for administrative control, including blacklisting and important notes'
        }),
        ('System properties', {
            'fields': ['created_by', 'modified_by', 'is_deleted', 'date_deleted', 'deleted_by'],
            'description': 'Tracks record lifecycle and user interactions, including creation and deletion details; '
                           'the fields are automatically updated upon user actions.'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]


@admin.register(SupplierFollower)
class SupplierFollowerAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'supplier', 'user', 'date_created']

    search_fields = ['supplier', 'user']

    autocomplete_fields = ['supplier', 'user']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Follower', {
            'fields': ['supplier', 'user'],
            'description': 'Follow a supplier to get updates on their activities'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]


@admin.register(SupplierRole)
class SupplierRoleAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'supplier', 'user', 'role', 'date_modified']

    list_filter = ['role']

    search_fields = ['supplier__name', 'user']

    autocomplete_fields = ['supplier', 'user']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Role', {
            'fields': ['supplier', 'user', 'role'],
            'description': 'Role of the user in the supplier organization'
        }),
        ('System properties', {
            'fields': ['created_by', 'modified_by'],
            'description': 'Tracks record lifecycle and user interactions, including creation and deletion details; '
                           'the fields are automatically updated upon user actions.'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]


@admin.register(SupplierAlternativeName)
class SupplierAlternativeNameAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'supplier', 'name', 'date_created', 'date_modified']

    search_fields = ['supplier__name', 'name']

    autocomplete_fields = ['supplier', 'created_by', 'modified_by']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Alternative name', {
            'fields': ['supplier', 'name'],
            'description': 'Role of the user in the supplier organization'
        }),
        ('System properties', {
            'fields': ['created_by', 'modified_by'],
            'description': 'Tracks record lifecycle and user interactions, including creation and deletion details; '
                           'the fields are automatically updated upon user actions.'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]


@admin.register(SupplierLocation)
class SupplierLocationAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'country', 'date_created', 'date_modified']

    list_filter = ['is_headquarters', 'country']

    filter_horizontal = []

    search_fields = ['name']

    autocomplete_fields = ['supplier', 'country', 'created_by', 'modified_by']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Location', {
            'fields': ['supplier', 'is_headquarters', 'address1', 'address2', 'city', 'subnational_region', 'postal_code', 'country'],
            'description': 'Role of the user in the supplier organization'
        }),
        ('Details', {
            'fields': ['name', 'description', 'website'],
            'description': 'Role of the user in the supplier organization'
        }),
        ('System properties', {
            'fields': ['created_by', 'modified_by'],
            'description': 'Tracks record lifecycle and user interactions, including creation and deletion details; '
                           'the fields are automatically updated upon user actions.'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]


@admin.register(SupplierFile)
class SupplierFileAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'supplier', 'name', 'date_created', 'date_modified']

    list_filter = ['is_deleted']

    search_fields = ['supplier', 'name', 'description']

    autocomplete_fields = ['supplier', 'created_by', 'modified_by', 'deleted_by']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('File', {
            'fields': ['supplier', 'name', 'description'],
            'description': 'Role of the user in the supplier organization'
        }),
        ('System properties', {
            'fields': ['created_by', 'modified_by', 'is_deleted', 'date_deleted', 'deleted_by'],
            'description': 'Tracks record lifecycle and user interactions, including creation and deletion details; '
                           'the fields are automatically updated upon user actions.'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]


@admin.register(SupplierFileVersion)
class SupplierFileVersionAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'supplier_file', 'version', 'date_created', 'date_modified']

    list_filter = ['is_deleted']

    search_fields = ['supplier_file', 'name', 'description']

    autocomplete_fields = ['supplier_file', 'created_by', 'modified_by', 'deleted_by']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('File', {
            'fields': ['supplier_file', 'file', 'version', 'description'],
            'description': 'Role of the user in the supplier organization'
        }),
        ('System properties', {
            'fields': ['created_by', 'modified_by', 'is_deleted', 'date_deleted', 'deleted_by'],
            'description': 'Tracks record lifecycle and user interactions, including creation and deletion details; '
                           'the fields are automatically updated upon user actions.'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]


@admin.register(SupplierContact)
class SupplierContactAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'supplier', 'name', 'email', 'date_created', 'date_modified']

    list_filter = ['is_deleted', ]

    search_fields = ['name', 'email', 'phone', 'description']

    autocomplete_fields = ['supplier', 'created_by', 'modified_by', 'deleted_by']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('File', {
            'fields': ['supplier', 'name', 'email', 'phone', 'description', 'show_email', 'show_phone',
                       'receive_inquiries'],
            'description': 'Role of the user in the supplier organization'
        }),
        ('System properties', {
            'fields': ['created_by', 'modified_by', 'is_deleted', 'date_deleted', 'deleted_by'],
            'description': 'Tracks record lifecycle and user interactions, including creation and deletion details; '
                           'the fields are automatically updated upon user actions.'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]


@admin.register(SupplierJob)
class SupplierJobAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'supplier', 'name', 'status', 'date_created', 'date_modified']

    search_fields = ['name', 'description']

    autocomplete_fields = ['supplier', 'country', 'created_by', 'modified_by', 'deleted_by']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Job', {
            'fields': ['supplier', 'name', 'tags', 'description', 'application_link', 'workplace_setting',
                       'employment_type', 'annual_salary_min', 'annual_salary_max', 'currency'],
            'description': 'Role of the user in the supplier organization'
        }),
        ('Location', {
            'fields': ['address1', 'address2', 'city', 'postal_code', 'country', 'subnational_region'],
            'description': 'Role of the user in the supplier organization'
        }),
        ('Status', {
            'fields': ['status', 'posting_start_date', 'posting_end_date'],
            'description': 'Role of the user in the supplier organization'
        }),
        ('System properties', {
            'fields': ['created_by', 'modified_by', 'is_deleted', 'date_deleted', 'deleted_by'],
            'description': 'Tracks record lifecycle and user interactions, including creation and deletion details; '
                           'the fields are automatically updated upon user actions.'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['name', 'code', 'parent']

    search_fields = ['name', 'code', 'description']

    autocomplete_fields = ['parent', 'created_by', 'modified_by', 'deleted_by']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Permission', {
            'fields': ['name', 'code', 'parent', 'description'],
            'description': 'Role of the user in the supplier organization'
        }),
        ('System properties', {
            'fields': ['created_by', 'modified_by', 'is_deleted', 'date_deleted', 'deleted_by'],
            'description': 'Tracks record lifecycle and user interactions, including creation and deletion details; '
                           'the fields are automatically updated upon user actions.'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'name', 'supplier']

    search_fields = ['name', 'description', 'supplier__name', 'permission__name', 'permission__code']

    autocomplete_fields = ['supplier', 'permission', 'created_by', 'modified_by', 'deleted_by']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Role', {
            'fields': ['name', 'supplier', 'permission', 'description'],
            'description': 'Role of the user in the supplier organization'
        }),
        ('System properties', {
            'fields': ['created_by', 'modified_by', 'is_deleted', 'date_deleted', 'deleted_by'],
            'description': 'Tracks record lifecycle and user interactions, including creation and deletion details; '
                           'the fields are automatically updated upon user actions.'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'date_modified', 'date_created']

    search_fields = ['role__name']

    autocomplete_fields = ['user', 'role', 'created_by', 'modified_by', 'deleted_by']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('User role', {
            'fields': ['user', 'role'],
            'description': 'Role of the user in the supplier organization'
        }),
        ('System properties', {
            'fields': ['created_by', 'modified_by', 'is_deleted', 'date_deleted', 'deleted_by'],
            'description': 'Tracks record lifecycle and user interactions, including creation and deletion details; '
                           'the fields are automatically updated upon user actions.'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]
