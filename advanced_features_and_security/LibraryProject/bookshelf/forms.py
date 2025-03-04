from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

    def clean_title(self):
        title = self.cleaned_data["title"]
        if "<script>" in title or "DROP TABLE" in title.upper():
            raise forms.ValidationError("Invalid input detected!")
        return title

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()