from apps.core.utils import AdminExportMixin
from django.contrib import admin

from .models import ArticleTag


# Admin objects
@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['name', 'slug', 'date_created', 'date_modified']

    list_filter = []

    filter_horizontal = []

    search_fields = ['name', 'slug']

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
            'fields': ['name', 'slug', 'description'],
            'description': 'Fields related to the property tag'
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
