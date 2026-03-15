from django.shortcuts import render, redirect
from .forms import StudentForm

def register_student(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("success")

    else:
        form = StudentForm()

    return render(request, "register.html", {"form": form})


def success(request):
    return render(request, "success.html")