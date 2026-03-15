from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentForm


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

    if request.method == "POST" and form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect("post_detail", slug=post.slug)

    return render(request, "post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form
    })