from django.test import TestCase
from catalog.models import Author,Book,Genre,BookInstance
# Create your tests here.
class AuthorModelTest(TestCase):

    @classmethod

    # called once at  the beginning of the test run for class-level setup, use when create 
    # objects that aren't modified or changed in any of the test methods
    def setUpTestData(cls):
        # set up non-modified objects used by all test methods
        Author.objects.create(first_name="Big", last_name="Bob")

    #called before every test function to set up any objects that may be modified by the test
    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'Died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)
   
    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id= 1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1/')

"""Create tests to models"""


class BookModelTest(TestCase):
    
    @classmethod
    
    def setUpTestData(cls):
        author = Author.objects.create(first_name="Jonathan",last_name="Felipe")
        #genrer1 = Genre.object.create(name="Education")
        #genrer2 = Genre.object.create(name="Mitology")
        book = Book.objects.create(title ='Test Book', author = author, summary = "Description to test", isbn = "1234567891012")
       

    def test_book_display_genre(self):
        book = Book.objects.get(id=1)
        genre1 = book.genre.create(name ="Education")
        genre2 = book.genre.create(name = "Mitology")
        expected_name=f'{genre1}, {genre2}'

        self.assertEquals(book.display_genre(), expected_name)

    def test_book_string_represent_model(self):
        book = Book.objects.get(id=1)
        expected_name= book.title
        
        self.assertEquals(str(book), book.title)

    def test_get_url_book(self):    
        book = Book.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(), '/catalog/book/1/')

"""Test to book instance"""
from django.contrib.auth.models import User,Group
import datetime
class BookInstanceTest(TestCase):
    
    @classmethod

    def setUpTestData(cls):
        author = Author.objects.create(first_name="Jonathan",last_name="Felipe")
        book = Book.objects.create(title ='Test Book', author = author, summary = "Description to test", isbn = "1234567891012")
       
        default_user = User.objects.create_user('default', password='default.password')
        default_user.is_staff = True

        user_library = User.objects.create_user('testlibrary', password='test.password')
        user_library.is_staff = True

        group = Group.objects.create(name='Library Members')
        group.user_set.add(user_library)
        

        book_instance1 = BookInstance.objects.create(borrower=User.objects.get(username='testlibrary'),book=book)
        book_instance2 = BookInstance.objects.create(borrower=User.objects.get(username='default'),book=book)

 #def test_all_get_absolute_url(self):
        #book = BookInstance.objects.filter(borrower="testlibrary")
        #self.assertEquals(book.get_absolute_url, "/catalog/mybooks/")