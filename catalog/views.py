from django.shortcuts import render
from django.views import generic
from catalog.models import Book, BookInstance, Genre, Author
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# Create your views here.
def index(request):
    """view function for home page of site"""
    
    num_books = Book.objects.filter(title='a').count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.all()

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

class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Book
    paginate_by = 1

class BookDetailView(generic.DetailView):
    """Generic class-based view for a detail of books."""
    model = Book

class AuthorListView(generic.ListView):
    """Generic class-based view for a list of Authors."""
    model = Author
    paginate_by = 1

class AuthorDetailView(generic.DetailView):
    
    model = Author

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic view listing books on loan to current user"""
    model = BookInstance
    paginate_by = 1
    template_name ='catalog/bookinstance_list_borrowed_user.html'

    def get_queryset(self):#restrict for user 
        return BookInstance.objects.filter(borrower = self.request.user).filter(status__exact= 'o').order_by('due_back')

class AllBooksBorrowedListView(PermissionRequiredMixin, generic.ListView):
    """Generic view listing all books borrowed for library members"""
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'#value to define on model book instance
    template_name = 'catalog/bookinstance_all_borrowed.html'

    def get_queryset(self):
        
        return BookInstance.objects.filter(status__exact='o').order_by('-due_back')
