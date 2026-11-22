from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel


@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'dob',
        'is_staff',
        'is_active',
    )

    search_fields = ('username', 'email')

    list_filter = ('is_staff', 'is_active')

    ordering = ('id',)

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('dob', 'profile_picture')
        }),
    )