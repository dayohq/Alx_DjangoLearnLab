from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Model representing an author.
    Each author has a name and can have multiple books.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    """
    Model representing a book.
    Each book has a title, publication year, and author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField(default=2000)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year}) by {self.author.name}"
    

    

    


