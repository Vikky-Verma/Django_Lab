from django.contrib import admin
from .models import Category, Post, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("title",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "post", "created_at")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)