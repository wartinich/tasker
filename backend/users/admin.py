from django.contrib.auth.admin import UserAdmin as StockUserAdmin

from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(StockUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('user_photo', 'username', 'first_name', 'last_name', 'date_of_birth')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'password2'),
        }),
    )