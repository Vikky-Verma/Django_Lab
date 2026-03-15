from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def home(request):

    posts = Post.objects.all()
    categories = Category.objects.all()

    return render(request, "home.html", {
        "posts": posts,
        "categories": categories
    })


def posts_by_category(request, slug):

    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all()

    return render(request, "category_posts.html", {
        "category": category,
        "posts": posts
    })



def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()

    form = CommentForm(request.POST or None)

    if request.method == "POST" and request.user.is_authenticated and form.is_valid():

        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()

        return redirect("post_detail", slug=post.slug)

    return render(request, "post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form
    })
    

def signup_view(request):

    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home")

    return render(request, "signup.html", {"form": form})

def login_view(request):

    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("home")

    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")