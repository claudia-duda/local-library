
from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from datetime import date,timedelta
from django.utils import timezone
from .Author import Author
from .Genre import Genre

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    book_photo = models.ImageField(upload_to='book-image/%d/%m/%Y/', blank=True, null= True)
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    
    date_here = models.DateField(default= date.today())

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """Create a string for the genre. required to display genre in admin"""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
       
    
    display_genre.short_description = 'Genre'