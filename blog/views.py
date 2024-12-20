from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from .models import Blog
from django.http import JsonResponse


def blog_home(request):
    all_blog = Blog.objects.all()
    return render(request, "blog/home.html", {"blogs": all_blog})


def post_detail(request, slug):
    all_blog = Blog.objects.all()
    blog = get_object_or_404(all_blog, slug=slug)
    return render(request, "blog/post_detail.html", {"blog": blog, "year": 2024})


def google_console(request):
    return render(request, "blog/googled207b771908af026.html")
