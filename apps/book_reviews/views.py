from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import Book, BookManager, Author, Review
from ..user_dashboard_app.models import User

# Create your views here.
def index(request):
    reviews = Review.objects.all().order_by('-id')[:3]
    books = Book.objects.all()

    context = {
        'reviews': reviews,
        'books': books
    }
    return render(request, 'book_reviews/index.html', context)
def add_book(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'book_reviews/add_book.html', context)
def create_book(request):
    if request.session.get('user'):
        user =  User.objects.get(id=request.session['user']['id'])
        print user.first_name
        book = Book.objects.validate(request.POST, user)
        if book[0]:
            new_book_id = book[2].id
            messages.success(request, 'New Review Created')
            return redirect('/books')
        else:
            for error in book[1]:
                messages.warning(request, error)
            return redirect('/books/add')
    else:
        messages.warning(request, 'You must be logged in!')
        return redirect('/books/add')
def purge_books(request):
    Book.objects.all().delete()
    Author.objects.all().delete()
    Review.objects.all().delete()
    return redirect('/dashboard')
def book(request, id):
    book = Book.objects.get(id=id)
    reviews = Review.objects.filter(book=id).order_by('-id')[:5]  
    context = {
        'book': book,
        'reviews': reviews
    }
    return render(request, 'book_reviews/book.html', context)
def submit_review(request, id):
    book = Book.objects.get(id=id)
    user =  User.objects.get(id=request.session['user']['id'])
    if len(request.POST['review']) < 10:
        messages.warning(request, 'Please provide a detailed review')
    else:
        new_review = Review.objects.create(book=book, rating=request.POST['rating'], reviewer=user, review=request.POST['review'])
    return redirect('/books/'+id)
def delete_review(request, id):
    Review.objects.get(id=id).delete()
    return redirect('/books')
