from django.contrib.auth.models import Group, User
from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Account


@admin.register(Account)
class AccountAdmin(ExportMixin, admin.ModelAdmin):
    fields = ['id', 'is_visible', 'email', 'first_and_last_name', 'uni_major', 'uni_name',
              'uni_position', 'is_verified', 'is_graduated', 'is_professor',
              'created_at', 'updated_at', 'notes']
    readonly_fields = ('id', 'first_and_last_name', 'uni_major', 'uni_name',
                       'uni_position', 'is_verified', 'is_graduated', 'is_professor',
                       'created_at', 'updated_at')
    list_display = ('email', 'first_and_last_name', 'is_verified', 'is_professor', 'is_visible',
                    'created_at', 'updated_at')
    list_filter = (
        ('is_professor', admin.BooleanFieldListFilter),
        ('is_verified', admin.BooleanFieldListFilter),
        ('is_visible', admin.BooleanFieldListFilter),
        ('is_graduated', admin.BooleanFieldListFilter),
    )
    search_fields = ('id', 'first_and_last_name', 'email', 'uni_major', 'uni_name', 'uni_position', 'notes')

    def has_add_permission(self, request, obj=None):
        return False


# admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
