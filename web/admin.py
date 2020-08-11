from django.contrib.auth.models import Group, User
from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    fields = ['id', 'email', 'first_and_last_name', 'uni_major', 'uni_name',
              'uni_position', 'is_visible', 'is_verified', 'is_graduated', 'is_professor',
              'created_at', 'updated_at', 'notes']
    readonly_fields = ('id', 'email', 'first_and_last_name', 'uni_major', 'uni_name',
                       'uni_position', 'is_visible', 'is_verified', 'is_graduated', 'is_professor',
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


admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
