from apps.core.utils import AdminExportMixin
from django.contrib import admin

from .models import ItemInquiry, SupplierInquiry


# Admin objects
@admin.register(ItemInquiry)
class ItemInquiryAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'supplier', 'item', 'is_processed', 'date_created', 'date_modified']

    list_filter = ['status']

    search_fields = ['name', 'email', 'organization', 'content']

    autocomplete_fields = ['inquirer', 'supplier', 'item', 'country', 'created_by', 'modified_by', 'deleted_by']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Inquiry', {
            'fields': ['supplier', 'item', 'inquirer', 'name', 'email', 'organization', 'position', 'country',
                       'content'],
            'description': 'Item inquiry information'
        }),
        ('Inquiry requests', {
            'fields': ['request_datasheet', 'request_icd', 'request_options_sheet', 'request_user_manual',
                       'request_cad_model', 'request_quotation', 'request_lead_time', 'request_heritage',
                       'number_of_flight_units', 'number_of_engineering_units'],
            'description': 'Specific requests for the item inquiry'
        }),
        ('Processing properties', {
            'fields': ['status', 'importance', 'is_inquirer_emailed', 'is_respondent_emailed'],
            'description': 'Inquiry processing information'
        }),
        ('Notes and custom data', {
            'fields': ['notes', 'custom_data'],
            'description': 'Additional information and custom data for the inquiry'
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


@admin.register(SupplierInquiry)
class SupplierInquiryAdmin(admin.ModelAdmin, AdminExportMixin):
    list_display = ['__str__', 'supplier', 'is_processed', 'date_created', 'date_modified']

    list_filter = ['status']

    search_fields = ['name', 'email', 'organization', 'content']

    autocomplete_fields = ['inquirer', 'supplier', 'country', 'created_by', 'modified_by', 'deleted_by']

    def export_as_csv(self, request, queryset):
        return AdminExportMixin.export_as_csv(self, request, queryset)

    def export_as_json(self, request, queryset):
        return AdminExportMixin.export_as_json(self, request, queryset)

    def export_as_text(self, request, queryset):
        return AdminExportMixin.export_as_text(self, request, queryset)

    actions = ['export_as_csv', 'export_as_json', 'export_as_text']

    readonly_fields = ['id', 'uuid', 'date_created', 'date_modified']

    fieldsets = [
        ('Inquiry', {
            'fields': ['supplier', 'inquirer', 'name', 'email', 'organization', 'position', 'country',
                       'content'],
            'description': 'General inquiry information'
        }),
        ('Processing properties', {
            'fields': ['status', 'importance', 'is_inquirer_emailed', 'is_respondent_emailed'],
            'description': 'Inquiry processing information'
        }),
        ('Notes and custom data', {
            'fields': ['notes', 'custom_data'],
            'description': 'Additional information and custom data for the inquiry'
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
