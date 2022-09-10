from django.contrib import admin
from accounts.models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    ordering = ('email',)
    # add_fieldsets = (
    #     (None, {'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')})
    # )
    # readonly_fields = ("last_login", "data_joined")
    # fieldsets = (
    #     (
    #         "Fields",
    #         {
    #             "fields": (
    #                 "email",
    #                 "date_joined",
    #                 "last_login",
    #                 "is_active",
    #                 "is_staff",
    #                 "is_superuser",
    #                 "groups",
    #                 "user_permissions",
    #                 "password",
    #             )
    #         },
    #     ),
    # )