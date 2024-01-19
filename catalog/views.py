from django.shortcuts import render
from django.views.generic.base import View

class Product( View ):
    pass
    def get( self, request ):
        return render(request, 'catalog/index.html')
        #return render(request, 'catalog/index.html', {'post_list': posts, 'comment_count': comment_count})