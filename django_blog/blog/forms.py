from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget  # Import TagWidget

class RegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]