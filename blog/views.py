from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Comments
from .form import CommentsForm

class PostView( View ):
    """выводы записей"""
    def get( self, request ):
        posts = Post.objects.all()
        comment_count = Comments.objects.count()
        return render(request, 'blog/blog.html', {'post_list': posts, 'commeent_list': comment_count})

class PostDetail( View ):
    """ вывод записей """
    def get(self, request, pk):
        post = Post.objects.get( id = pk )
        return render( request, 'blog/blog_detail.html', { 'post': post } )
    
class AddComments(View):
    """Добавление коментариев"""
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect( f'/{pk}')
    