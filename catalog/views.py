from django.shortcuts import render,get_object_or_404
from django.views import generic
from catalog.models import Book, BookInstance, Genre, Author
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
#for forms
import datetime
from .forms import RenewBookForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required

# Create your views here.
def index(request):
    """view function for home page of site"""
    
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()


    #number of visits 
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available':num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }    

    return render(request , 'index.html' , context=context)

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date'] # or due_bacck in modelform case 
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date}) # or due_bacck in modelform case 

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)
            

class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    paginate_by = 5

class BookDetailView(generic.DetailView):
    """Generic class-based view for a detail of books."""
    model = Book

class AuthorListView(generic.ListView):
    """Generic class-based view for a list of Authors."""
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    
    model = Author

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic view listing books on loan to current user"""
    model = BookInstance
    paginate_by = 10
    template_name ='catalog/bookinstance_list_borrowed_user.html'

    def get_queryset(self):#restrict for user 
        return BookInstance.objects.filter(borrower = self.request.user).filter(status__exact= 'o').order_by('due_back')

class AllBooksBorrowedListView(PermissionRequiredMixin, generic.ListView):
    """Generic view listing all books borrowed for library members"""
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'#value to define on model book instance
    template_name = 'catalog/bookinstance_all_borrowed.html'
    paginate_by = 5

    def get_queryset(self):

        return BookInstance.objects.filter(status__exact='o').order_by('-due_back')



""" generic View to create a new a model object for edit,create and delede based in models"""

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from catalog.models import Author

""" Create Update and Delete to Authors"""

class AuthorCreate(PermissionRequiredMixin,CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018'}
    template_name= 'catalog/default-forms/default_form.html'
    permission_required = 'catalog.can_mark_returned'

class AuthorUpdate(PermissionRequiredMixin,UpdateView):
    model = Author
    fields = ['first_name' , 'last_name' , 'date_of_birth' , 'date_of_death']   
    template_name = 'catalog/default-forms/default_form.html'
    permission_required = 'catalog.can_mark_returned'
class AuthorDelete(PermissionRequiredMixin,DeleteView):
    model = Author
    template_name= 'catalog/default-forms/default_confirm_delete.html'
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('authors')# redirect to list authors
    


""" Create Update and Delete to Authors"""

class BookCreate(PermissionRequiredMixin,CreateView):
    model= Book
    fields ='__all__'
    initial = {'summary':'brief description'}
    template_name= 'catalog/default-forms/default_form.html'
    permission_required = 'catalog.can_mark_returned'
class BookUpdate(PermissionRequiredMixin,UpdateView):
    model=Book
    fields = ['title', 'author', 'isbn']
    template_name= 'catalog/default-forms/default_form.html'
    permission_required = 'catalog.can_mark_returned'

class BookDelete(PermissionRequiredMixin,DeleteView):
    model=Book
    template_name= 'catalog/default-forms/default_confirm_delete.html'
    success_url = reverse_lazy('books')# redirect to list authors
    permission_required = 'catalog.can_mark_returned'
