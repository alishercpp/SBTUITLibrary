from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from unfold.admin import ModelAdmin

from .forms import StudentCreationForm, StudentChangeForm
from .models import Student


@admin.register(Student)
class StudentAdmin(UserAdmin, ModelAdmin):
    add_form = StudentCreationForm
    form = StudentChangeForm
    model = Student
    list_display = ['username', 'first_name', 'last_name', 'middle_name', 'is_superuser', 'is_staff']
    fieldsets = (
        ('Talabani tahrirlash', {
            'fields': ('first_name', 'last_name', 'middle_name'),
        }),
    )
    add_fieldsets = (
        ('Yangi talaba qo\'shish', {
            "classes": ("wide", ),
            "fields": (
                'password1', 'password2',
                'first_name', 'last_name', 'middle_name',
            ),
        }),
    )
    search_fields = ("username", 'first_name', 'last_name', 'middle_name', )
    ordering = ('username', )

# admin.site.register(Student, StudentAdmin)