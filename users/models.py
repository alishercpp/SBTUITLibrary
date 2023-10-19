from django.db import models
from .managers import StudentManager
from django.contrib.auth.models import AbstractUser
from random import choice

def tokenize():
    token = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in range(6):
        token += choice(letters)
    return token

ROLES = (
    ('admin', 'Admin'),
    ('teacher', 'Teacher'),
    ('student', 'Student'),
)

class Student(AbstractUser):
    username    = models.CharField(max_length=30, unique=True, null=False, blank=False, default=tokenize)
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    degree      = models.CharField(max_length=100)
    role        = models.CharField(max_length=20, choices=ROLES)

    objects = StudentManager()

    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username
    