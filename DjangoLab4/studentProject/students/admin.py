from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "age", "course", "phone")

admin.site.register(Student, StudentAdmin)