from apps.core.utils import AdminExportMixin
from django.contrib import admin

from .models import FeedbackMessage, SupportMessage


# Admin objects
@admin.register(FeedbackMessage)
class FeedbackMessageAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'page_url', 'category', 'date_created']

    list_filter = ['category', 'status']

    search_fields = ['name', 'email', 'page_url', 'content']

    autocomplete_fields = ['user']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Feedback', {
            'fields': ['user', 'name', 'email', 'page_url', 'category', 'content'],
            'description': 'Fields related to the property tag'
        }),
        ('Feedback status', {
            'fields': ['status', 'date_completed', 'date_archived'],
            'description': 'Fields related to the property tag'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]

@admin.register(SupportMessage)
class SupportMessageAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'subject', 'status', 'date_created']

    list_filter = ['status']

    search_fields = ['name', 'email', 'page_url', 'content']

    autocomplete_fields = ['user']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Support message', {
            'fields': ['user', 'name', 'email', 'page_url', 'subject', 'content'],
            'description': 'Fields related to the property tag'
        }),
        ('Support message status', {
            'fields': ['status', 'date_completed'],
            'description': 'Fields related to the property tag'
        }),
        ('Ready-only properties', {
            'fields': ['id', 'uuid', 'date_created', 'date_modified'],
            'description': 'System-generated fields that are crucial for data integrity and are not editable'
        })
    ]
