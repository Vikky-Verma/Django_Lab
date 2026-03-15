from django.shortcuts import render, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'students/detail.html', {'student': student})
