from django.shortcuts import render
from django.views.generic.base import View
from .models import Post

class PostView(View):
    """выводы записей"""
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})

