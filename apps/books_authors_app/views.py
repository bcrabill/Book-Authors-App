from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books_authors_app/index.html', context)

def authors(request):
    
    return render('authors.html')

def bookspage(request, book_id):
    context = {
        'book_page' : Book.objects.get(id='book_id')
    }
    return render(request, 'books_authors_app/books.html', context)

def add_books(request):
    if request.method == "POST":
        Book.objects.create(title = request.POST['title'],
        description = request.POST['description'])
        print(request.POST)
        return redirect(request, 'index.html')
        
    
    return render(request, "index.html", context)

def add_authors(request):
    if request.method == "POST":
        context = {
            Author.object.create(first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            notes = request.POST['notes'])          
        }
        print(request.POST)
        return redirect('/')

    return render(request, 'index.html', context)



