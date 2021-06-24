from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404

# Create your views here.
from book.forms import EmailPostForm
from book.models import Book


def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'books': books,
        'page_obj': page_obj
    }
    return render(request, 'Book/all_books.html', context)


def book_detail(request, id, name):
    try:
        book = Book.objects.get(id=id, name=name)
    except Book.DoesNotExist:
        return HttpResponseRedirect('/404')
    related_book = Book.objects.get_queryset().filter(tag__title=book).distinct()
    context = {
        'book': book,
        'related_book': related_book,
    }
    return render(request, 'Book/book.html', context)


def post_share(request, id):
    # Retrieve post by id
    post = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
    else:
        form = EmailPostForm()
    return render(request, 'Book/share.html', {'post': post, 'form': form})


def tag_list_book(request, slug):
    books = Book.objects.filter(tag__slug=slug).distinct()
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'books': books,
        'page_obj': page_obj
        # 'books': books
    }
    return render(request,'Book/all_books.html',context)