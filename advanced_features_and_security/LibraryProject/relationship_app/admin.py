from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    """Customize admin panel for managing CustomUser."""
    model = CustomUser
    list_display = ("email", "username", "date_of_birth", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "date_of_birth", "profile_photo", "is_staff", "is_active"),
        }),
    )
    search_fields = ("email", "username")
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)