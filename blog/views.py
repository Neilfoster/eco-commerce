from django.shortcuts import render
from .models import Blog
from django.contrib.auth.decorators import login_required
from . import forms


def blog(request):
    blog = Blog.objects.all()
    return render(request, "blog/blog.html", {"blog": blog})

@login_required(login_url="/accounts/login")
def create_blog(request):
    if request.method == 'POST':
        form = forms.CreateBlog(request.POST, request.FILES)
        blog = Blog.objects.all()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return render(request, "blog/blog.html", {'blog': blog})
    else:
        form = forms.CreateBlog()
    return render(request, 'blog/create_blog.html', {'form': form})