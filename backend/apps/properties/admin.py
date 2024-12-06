from apps.core.utils import AdminExportMixin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import (
    FloatProperty,
    IntegerProperty,
    Property,
    PropertyAlternativeName,
    PropertyLibrary,
    PropertySet,
    StringProperty,
)


class NonePropertyValueFilter(admin.SimpleListFilter):
    title = _('Property Value is None')
    parameter_name = 'property_value_is_none'

    def lookups(self, request, model_admin):
        return (
            ('yes', _('Yes')),
            ('no', _('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(
                integer_property__default_value__isnull=True,
                float_property__default_value__isnull=True,
                string_property__default_value__isnull=True,
                # Add checks for default values of other property types
            )
        if self.value() == 'no':
            return queryset.exclude(
                integer_property__default_value__isnull=True,
                float_property__default_value__isnull=True,
                string_property__default_value__isnull=True,
                # Add checks for default values of other property types
            )


# Admin objects
@admin.register(PropertyLibrary)
class PropertyLibraryAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['name', 'key', 'date_created', 'date_modified']

    list_filter = []

    filter_horizontal = []

    search_fields = ['name', 'slug', 'key', 'description']

    autocomplete_fields = ['created_by', 'modified_by', 'deleted_by']

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
        ('Library', {
            'fields': ['name', 'slug', 'key', 'is_builtin', 'status', 'description'],
            'description': 'Fields related to the property tag'
        }),
        ('Admin properties', {
            'fields': ['admin_notes'],
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


@admin.register(PropertySet)
class PropertySetAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['name', 'key', 'date_created', 'date_modified']

    list_filter = []

    filter_horizontal = []

    search_fields = ['name', 'key', 'description']

    autocomplete_fields = ['properties', 'created_by', 'modified_by']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Property set', {
            'fields': ['name', 'key', 'properties', 'description'],
            'description': 'Fields related to the property tag'
        }),
        ('Admin properties', {
            'fields': ['admin_notes'],
            'description': 'Settings and flags for administrative control, including blacklisting and important notes'
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


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['name', 'key', 'property_type', 'date_created', 'date_modified']

    list_filter = [NonePropertyValueFilter]

    filter_horizontal = []

    search_fields = ['name', 'slug', 'key', 'description']

    autocomplete_fields = ['library', 'created_by', 'modified_by']

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
        ('Property', {
            'fields': ['name', 'slug', 'key', 'library', 'is_builtin', 'property_type', 'status', 'description'],
            'description': 'Fields related to the property tag'
        }),
        ('Admin properties', {
            'fields': ['admin_notes'],
            'description': 'Settings and flags for administrative control, including blacklisting and important notes'
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


@admin.register(PropertyAlternativeName)
class PropertyAlternativeNameAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'property', 'date_created', 'date_modified']

    list_filter = []

    filter_horizontal = []

    search_fields = []

    autocomplete_fields = ['property', 'created_by', 'modified_by']

    prepopulated_fields = {}

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
            'fields': ['property', 'name', 'description'],
            'description': 'Fields related to the property tag'
        }),
        ('Admin properties', {
            'fields': ['admin_notes'],
            'description': 'Settings and flags for administrative control, including blacklisting and important notes'
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


@admin.register(IntegerProperty)
class IntegerPropertyAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'date_created', 'date_modified']

    list_filter = []

    filter_horizontal = []

    search_fields = ['property__name', 'property__slug', 'property__key']

    autocomplete_fields = ['property', 'created_by', 'modified_by']

    prepopulated_fields = {}

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Property value and settings', {
            'fields': ['property', 'default_value', 'is_min_limit_enabled', 'is_max_limit_enabled', 'min_limit_value',
                       'max_limit_value'],
            'description': 'Fields related to the property tag'
        }),
        ('Property units', {
            'fields': ['units_prefix', 'units_suffix'],
            'description': 'Fields related to the property tag'
        }),
        # ('Admin properties', {
        #     'fields': ['admin_notes'],
        #     'description': 'Settings and flags for administrative control, including blacklisting and important notes'
        # }),
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


@admin.register(FloatProperty)
class FloatPropertyAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'date_created', 'date_modified']

    list_filter = []

    filter_horizontal = []

    search_fields = ['property__name', 'property__slug', 'property__key']

    autocomplete_fields = ['property', 'created_by', 'modified_by']

    prepopulated_fields = {}

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Property value and settings', {
            'fields': ['property', 'default_value', 'step_size', 'is_min_limit_enabled', 'is_max_limit_enabled',
                       'min_limit_value', 'max_limit_value'],
            'description': 'Fields related to the property tag'
        }),
        ('Property units', {
            'fields': ['units_prefix', 'units_suffix'],
            'description': 'Fields related to the property tag'
        }),
        # ('Admin properties', {
        #     'fields': ['admin_notes'],
        #     'description': 'Settings and flags for administrative control, including blacklisting and important notes'
        # }),
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


@admin.register(StringProperty)
class StringPropertyAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'date_created', 'date_modified']

    list_filter = []

    filter_horizontal = []

    search_fields = ['property__name', 'property__slug', 'property__key']

    autocomplete_fields = ['property', 'created_by', 'modified_by']

    prepopulated_fields = {}

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Property value and settings', {
            'fields': ['property', 'default_value'],
            'description': 'Fields related to the property tag'
        }),
        # ('Admin properties', {
        #     'fields': ['admin_notes'],
        #     'description': 'Settings and flags for administrative control, including blacklisting and important notes'
        # }),
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
