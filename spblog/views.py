from django.shortcuts import render
from spblog.models import Blog

def spblog_index(request):
    blogs = Blog.objects.all()
    print('hey from spblog_index')
    context = {
            'blogs': blogs,
            }
    return render(request, 'spblog/spblog_index.html', context)

def spblog_detail(request, pk):
    print('hey from spblog_index')
    blog = Blog.objects.get(pk=pk)
    context = {
            'blog': blog,
            }
    return render(request, 'spblog/spblog_detail.html', context)
