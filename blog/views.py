from django.http import HttpResponse
from django.template import Context, loader
from .models import Book

def index(request):
    books = Book.objects.all()
    html = loader.get_template('blog/index.html')
    db = Context({'books': books})
    return HttpResponse(html.render(db))

def math(request):
    books = Book.objects.filter(text='Just for Vlad')
    html = loader.get_template('blog/header/math.html')
    db = Context({'books': books})
    return HttpResponse(html.render(db))

def physics(request):
    books = Book.objects.all()
    html = loader.get_template('blog/header/physics.html')
    db = Context({'books': books})
    return HttpResponse(html.render(db))

def natural(request):
    books = Book.objects.filter(text='Just for Vlad')
    html = loader.get_template('blog/header/natural.html')
    db = Context({'books': books})
    return HttpResponse(html.render(db))

def other(request):
    books = Book.objects.filter(text= 'Just for Vlad')
    html = loader.get_template('blog/header/other.html')
    db = Context({'books': books})
    return HttpResponse(html.render(db))

def contacts(request):
    books = Book.objects.filter(text='Just for Vlad')
    html = loader.get_template('blog/header/contacts.html')
    db = Context({'books': books})
    return HttpResponse(html.render(db))
