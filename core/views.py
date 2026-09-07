from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.forms import BookForm
from core.models import Book

@login_required
def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid() == True:
            name = form.cleaned_data['name']
            genre = form.cleaned_data['genre']
            book, _ = Book.objects.get_or_create(name=name, genre=genre)

            if not request.user.books.filter(id=book.id).exists():
                request.user.books.add(book)
                return render(request, 'partials/book-row.html', {'book': book})

    books = request.user.books.all()
    context = {'books': books, 'form': BookForm()}
    return render(request, 'index.html', context)