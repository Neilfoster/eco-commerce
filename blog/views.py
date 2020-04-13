from django.shortcuts import render
from .models import Blog
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login")
def blog(request):
    blog = Blog.objects.all()
    return render(request, "blog/blog.html", {"blog": blog})

