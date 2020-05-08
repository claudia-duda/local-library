from django.urls import path
from . import views

"""default Acess"""
urlpatterns = [
    path('' , views.index, name='index'),
    path('books/' , views.BookListView.as_view(), name='books'),    
    path('authors/', views.AuthorListView.as_view(), name='authors'),   
  
]

"""Crud to authors"""
urlpatterns += [
    path('author/create/' , views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/' , views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/<int:pk>/update/' , views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/' , views.AuthorDelete.as_view(), name='author-delete'),
]

"""Crud to books"""
urlpatterns+=[
    path('book/create/' , views.BookCreate.as_view() , name='book-create'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/update/' , views.BookUpdate.as_view() , name='book-update'),
    path('book/<int:pk>/delete/' , views.BookDelete.as_view() , name='book-delete'),

]
"""Crud to Renew"""
urlpatterns+=[
    #create
    path('allbooks/', views.AllBooksBorrowedListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/' , views.renew_book_librarian, name='renew-book-librarian'),  
    #delete
]
""" Acess to User"""
urlpatterns+=[
    path('mybooks/' , views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    #profile
]
