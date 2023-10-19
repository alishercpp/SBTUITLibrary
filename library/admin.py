from django.contrib import admin
from unfold.admin import ModelAdmin
from django.utils.html import mark_safe
from datetime import datetime

from .models import (
    Book,
    Order,
)

@admin.register(Book)
class BookModelAdmin(ModelAdmin):
    list_display = ['name', 'isbn']
    list_filter = ['name', 'author', 'created_at']
    search_fields = ['name', 'isbn', 'author']

@admin.register(Order)
class OrderModelAdmin(ModelAdmin):
    list_display = ['oid', 'student', 'book', 'scheduled_at', 'timed_out', 'status']
    search_fields = ['oid']
    list_filter = ['oid', 'student', 'book', ]

    def timed_out(self, obj):
        now = datetime.now().date()
        if now == obj.scheduled_at:
            return mark_safe("<b class='text-red-600'>Timed Out</b>")
        return mark_safe('<b class="text-green-600">Reading</b>')
