from django.shortcuts import render, get_object_or_404
from .models import BlogPage


def all_blogs(request):
    blogs = BlogPage.objects.order_by('-blog_date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs}, )


def detail(request, blog_id):
    blog = get_object_or_404(BlogPage, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
