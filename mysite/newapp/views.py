from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator

# Create your views here.


def book_list(request):
    book_object = Book.objects.all()
    book_name = request.GET.get('book_name')
    if book_name != '' and book_name is not None:
        book_object = book_object.filter(name__icontains=book_name)
    paginator = Paginator(book_object, 5)
    page = request.GET.get('page')
    book_object = paginator.get_page(page)
    return render(request, 'newapp/booklist.html', {'book_object': book_object})
