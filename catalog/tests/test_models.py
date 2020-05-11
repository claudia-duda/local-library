from django.test import TestCase
from catalog.models import Author,Book
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

    def test_det_absolute_url(self):
        author = Author.objects.get(id= 1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1/')

"""Create tests to models"""
#class BookModelTest(TestCase):
    
    #@classmethod
    #def setUpTestData(cls):
    #    Book.objects.create()  
    