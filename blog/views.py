from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Comments, Likes
from .form import CommentsForm

class PostView( View ):
    """выводы записей"""
    def get( self, request ):
        posts = Post.objects.all()
        comment_count = Comments.objects.count()
        return render(request, 'blog/blog.html', {'post_list': posts, 'comment_count': comment_count})

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
    
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_clietn = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_clietn, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_Like = Likes()
            new_Like.ip = ip_clietn
            new_Like.pos_id = int(pk)
            new_Like.save()
            return redirect(f'/{pk}')  

class DelLike(View):
    def get(self, request, pk):
        ip_clietn = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_clietn)
            lik.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')