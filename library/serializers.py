from rest_framework.serializers import ModelSerializer

from .models import (
    Book,
    Order,
)


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['book', 'student', 'oid', 'created_at', 'scheduled_at', 'is_ended', 'status']
