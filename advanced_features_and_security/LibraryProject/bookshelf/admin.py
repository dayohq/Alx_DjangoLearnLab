from django.contrib import admin
from .models import CustomUser, CustomUserManager

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    search_fields = ('title', 'author')  # Enable search by title and author
    list_filter = ('publication_year',)  # Add filter by publication year

class CustomUserAdmin(admin.ModelAdmin):
    list_display =('username', 'email', 'date_of_birth', 'profile_photo')
    
admin.site.register(CustomUser, CustomeUserAdmin)

    