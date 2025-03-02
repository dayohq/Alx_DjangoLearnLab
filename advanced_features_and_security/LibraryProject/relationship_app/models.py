from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings



# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book Model with ForeignKey to Author
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title

#Library Model with ManyToManyField to Book
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

#Librarian Model with OnetoOneField to Library
class Librarian(models.Model):
    name  = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Define user roles
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Automatically create a UserProfile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


# Custom User Manager
class CustomUserManager(BaseUserManager):
    """Manager for custom user model with email-based authentication."""

    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        """Creates and returns a regular user with given details."""
        if not email:
            raise ValueError(_("The Email field must be set"))
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """Creates and returns a superuser with admin privileges."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(username, email, password, **extra_fields)

# Custom User Model
class CustomUser(AbstractUser):
    """Custom user model replacing Django's default User model."""
    email = models.EmailField(unique=True)  # Unique Email instead of username-based login
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

