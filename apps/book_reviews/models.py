from __future__ import unicode_literals

from django.db import models
# from user_dashboard_app.models import models as user_models

class ReviewManager(models.Manager):
    def validate(self):
        pass

class BookManager(models.Manager):
    def validate(self, data, user):
        errors = []
        book_title = data['book-title']
        author = data['author']
        other_author = data['other-author']
        review_details = data['review']
        rating = int(data['rating'])

        if len(book_title) < 1:
            errors.append('Please enter a title')
        if len(review_details) < 10:
            errors.append('Please provide a detailed review')
        if len(author) < 1 and len(other_author) < 1:
            errors.append('Please choose from the list or enter an author')
        elif len(author) > 1 and len(other_author) > 1:
            errors.append('Please use only the drop OR the other field')
        elif len(author) > 1 and len(other_author) == 0:
            select_author = Author.objects.get(id=int(author))
        elif len(author) == 0 and len(other_author) > 1:
            select_author = Author.objects.create(name=other_author)
        if not errors:
            new_book = Book.objects.create(title=book_title, author=select_author)
            new_review = Review.objects.create(book=new_book, rating=rating, reviewer=user, review=review_details)
            return (True, errors, new_book)
        else:
            return (False, errors)

class AuthorManager(models.Manager):
    def validate(self):
        pass

class Author(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()
    class Meta:
        managed = True
        db_table = 'authors'

class Book(models.Model):
    title = models.CharField(max_length=45, blank=True, null=True)
    author = models.ForeignKey(Author)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author)
    objects = BookManager()

    class Meta:
        managed = True
        db_table = 'books'

class Review(models.Model):
    book = models.ForeignKey(Book)
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    review = models.TextField(max_length=60, blank=True, null=True)
    reviewer = models.ForeignKey('user_dashboard_app.User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

    class Meta:
        managed = True
        db_table = 'reviews'
