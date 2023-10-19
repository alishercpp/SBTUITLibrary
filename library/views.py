from django.shortcuts import render
from faker import Faker

from .models import (
    Book,
    Order,
)


def home(request):
    # for i in range(100):
    #     fake = Faker()
    #     Book.objects.create(
    #         name=fake.name(),
    #         author=fake.name(),
    #         isbn=fake.name() + f"{i}",
    #     )
    book = request.GET.get('book')
    print(book)
    books = None
    if book:
        books = Book.objects.all()
    return render(request, 'home.html', {
        'books': books
    })