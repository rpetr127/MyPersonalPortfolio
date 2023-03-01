from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.decorators.csrf import csrf_exempt


csrf_exempt
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
   blog =  get_object_or_404(Blog, pk=blog_id)
   return render(request, 'blog/detail.html', {'id': blog_id, 'blog': blog})