import uuid # Required for unique book instances
from django.db import models
from datetime import datetime,date
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .Book import Book
from pessoas.models import Pessoa



class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True, help_text="Enter a date between now and 4 weeks (default 3).")

    
    

    def clean_renewal_date(self):#validation : clean_nameField()
        
        data = self.cleaned_data['due_back']
        #check if a date isn't' in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        
        #check if a te isn't in the allowed range (+4 weeks from today)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data


    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:            
           return True

        return False  
          
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned" , "Set book as returned"),)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('all-borrowed')