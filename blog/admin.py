from django.contrib import admin
from .models import Post, Comments

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('post', 'name')