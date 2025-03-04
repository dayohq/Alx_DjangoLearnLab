from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.http import HttpResponse

# Create your views here.
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    return HttpResponse("Welcome to my book shelf.")
