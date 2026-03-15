from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<slug:slug>/", views.posts_by_category, name="category_posts"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
]