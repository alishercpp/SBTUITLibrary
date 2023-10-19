from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .models import (
    Book,
    Order,
)
from .serializers import (
    BookModelSerializer,
    OrderModelSerializer,
)


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ['name']

class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ['is_ended']
