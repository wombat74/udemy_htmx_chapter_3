from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    books = request.user.books.all()
    context = {'books': books}
    return render(request, 'index.html', context)