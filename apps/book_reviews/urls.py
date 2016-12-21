from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add$', views.add_book, name = 'add-book'),
    url(r'^create_book$', views.create_book, name = 'create_book'),
    url(r'^(?P<id>\d+$)', views.book, name = 'book'),
    url(r'^submit_review/(?P<id>\d+$)', views.submit_review, name='submit_review'),
    url(r'^delete_review/(?P<id>\d+$)', views.delete_review, name='delete_review'),
    url(r'^purge_books$', views.purge_books, name = 'purge_books'),

]
