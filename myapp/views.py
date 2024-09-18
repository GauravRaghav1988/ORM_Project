from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Author,Book
import json

def orm(request):
    authors = Author.objects.all()
    books_with_author = Book.objects.select_related('author').all()
    context = {
        'authors': authors,
        'books_with_author': books_with_author,
    }
    return render(request, 'home.html', context)


def specific_author(request,author_id):
    # breakpoint()
    author = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(author=author)
    context = {
        'author': author,
        'book_by_author':books
    }
    # breakpoint()
    # print(context)
    return render(request, 'user_id.html', context)


def list_author(request):
    return JsonResponse({"msg":True, "data":list()}) 

def get_author(request, author_id):
    pass 

def create_author(request):
    pass

def update_author(request, author_id):
    pass

def patch_author(request, author_id):
    pass

def delete_author(request, author_id):
    pass




def list_book(request, book_id):
    pass 

def get_book(request, book_id):
    pass 

def create_book(request):
    pass

def update_book(request, book_id):
    pass

def patch_book(request, book_id):
    pass

def delete_book(request, author_id):
    pass





# author_by_name = Author.objects.get(name="J.K. Rowling")
# books = Book.objects.all()
# books_by_author = Book.objects.filter(author__name="J.K. Rowling")
# book = Book.objects.get(title="1984")
# old_authors = Author.objects.filter(birth_date__lt="1900-01-01")
# exists = Book.objects.filter(title="1984").exists()
# books = Book.objects.select_related('author').all()  #onetoone, and foreign key
# books = Book.objects.prefetch_related('genres').all() #manytomany
