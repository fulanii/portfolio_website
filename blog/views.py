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


def blog_login(request):
    if request.method == "POST":
        username  = request.POST.get('username')
        password  = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['name'] = username
            return redirect(reverse('dashboard'))
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid username or password.'})
        
    return render(request, "blog/login.html")


def blog_logout(request):
    logout(request)
    return redirect('login')


@login_required
def blog_dashboard(request):
    name = request.session.get('name')
    return render(request, "blog/dashboard.html", {"name": name})


@require_http_methods(["POST"])
def submit_blog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')  # This contains the HTML from CKEditor

        try:
            Blog.objects.create(title=title, content=content)
            return JsonResponse({"status": "success", "message": "Blog published successfully!"})
        except Exception as eror:
            return JsonResponse({"status": "error", "message": f"Something went wrong: str({eror})"})
        
    return JsonResponse({"status": "error", "message": "Invalid request method."})


def post_detail(request, slug):
    all_blog = Blog.objects.all()
    blog = get_object_or_404(all_blog, slug=slug)
    return render(request, 'blog/post_detail.html', {'blog': blog})