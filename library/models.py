from django.db import models
from users.models import Student
from random import choice

def tokenize():
    token = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in range(6):
        token += choice(letters)
    return token

def save_file(instnce, filename):
    return '/'.join(['books', f"{instnce.pk}", filename])

class Book(models.Model):
    name = models.CharField(max_length=1000)
    isbn = models.CharField(max_length=50, unique=True, error_messages={"unique": "Ikkita bir xil kitob kiritishning iloji yuq"})
    author = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True, default='')
    is_e = models.BooleanField(default=False)
    file = models.FileField(upload_to=save_file, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    oid          = models.CharField(max_length=20, default=tokenize, editable=False)
    description  = models.TextField(null=True, blank=True, default='')
    book         = models.ForeignKey(Book, on_delete=models.CASCADE)
    student      = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at    = models.DateField(auto_now_add=True)
    scheduled_at = models.DateField()
    is_ended     = models.BooleanField(default=False)
    

    def __str__(self):
        return self.oid
    
    def status(self):
        from datetime import datetime
        now = datetime.now().date()
        if now == self.scheduled_at:
            return 'timed_out'
        return 'reading'
