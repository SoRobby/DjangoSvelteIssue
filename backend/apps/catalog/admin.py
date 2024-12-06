from apps.core.utils import AdminExportMixin
from django.contrib import admin

from .models import (
    ItemProperty,
    ItemPropertyGroup,
    LaunchVehicleItem,
    SpaceVehicleItem,
    Taxonomy,
    TaxonomyItem,
    TaxonomyItemFile,
    TaxonomyItemFileVersion,
    TaxonomyNode,
    TaxonomyNodeAlternativeName,
)


# Admin objects
@admin.register(Taxonomy)
class TaxonomyAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['name', 'slug', 'date_created', 'date_modified']

    list_filter = []

    filter_horizontal = []

    search_fields = ['name']

    autocomplete_fields = ['created_by', 'modified_by']

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
            'fields': ['name', 'slug', 'key', 'description'],
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


@admin.register(TaxonomyNode)
class TaxonomyNodeAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['name', 'slug', 'date_created', 'date_modified']

    list_filter = ['taxonomy__name', ]

    filter_horizontal = []

    search_fields = ['name']

    autocomplete_fields = ['taxonomy', 'parent', 'created_by', 'modified_by']

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
        ('Taxonomy', {
            'fields': ['taxonomy'],
            'description': 'Taxonomy to which the node belongs'
        }),
        ('Node', {
            'fields': ['parent', 'name', 'slug', 'key', 'status', 'weight', 'description'],
            'description': 'Node properties and settings'
        }),
        ('Admin properties', {
            'fields': ['admin_notes'],
            'description': 'Settings and flags for administrative control'
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


@admin.register(TaxonomyNodeAlternativeName)
class TaxonomyNodeAlternativeNameAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['name', 'node', 'date_created', 'date_modified']

    list_filter = ['node__taxonomy__name', ]

    filter_horizontal = []

    search_fields = ['name', 'description', 'node__name', 'node__slug', 'node__key']

    autocomplete_fields = ['node', 'created_by', 'modified_by']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Node alternative name', {
            'fields': ['node', 'name', 'description'],
            'description': 'Fields related to the property tag'
        }),
        ('Admin properties', {
            'fields': ['admin_notes'],
            'description': 'Settings and flags for administrative control'
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


@admin.register(TaxonomyItem)
class TaxonomyItemAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['name', 'node', 'date_created', 'date_modified']

    list_filter = [
        ('node', admin.EmptyFieldListFilter),
        ('node__taxonomy', admin.RelatedOnlyFieldListFilter)
    ]

    filter_horizontal = []

    search_fields = ['name', 'slug', 'description']

    autocomplete_fields = ['taxonomy_object', 'node', 'created_by', 'modified_by']

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
        ('Item', {
            'fields': ['taxonomy_object', 'node', 'name', 'slug', 'status', 'visibility', 'description', 'cached_properties'],
            'description': 'Fields related to the property tag'
        }),
        ('Admin properties', {
            'fields': ['admin_notes'],
            'description': 'Settings and flags for administrative control'
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


@admin.register(SpaceVehicleItem)
class SpaceVehicleItemAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'node', 'date_created', 'date_modified']

    list_filter = []

    filter_horizontal = []

    search_fields = ['name', 'slug', 'description']

    autocomplete_fields = ['taxonomy_object', 'node', 'supplier', 'created_by', 'modified_by', 'deleted_by']

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
        ('Node', {
            'fields': ['taxonomy_object', 'node'],
            'description': 'Node the item is correlated to'
        }),
        ('Item', {
            'fields': ['name', 'slug', 'description', 'supplier'],
            'description': 'Fields related to the property tag'
        }),
        ('Properties', {
            'fields': ['is_flight_proven'],
            'description': 'Fields related to the property tag'
        }),
        ('Admin properties', {
            'fields': ['admin_notes'],
            'description': 'Settings and flags for administrative control'
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


