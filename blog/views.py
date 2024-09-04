from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.urls import reverse

# Create your views here.
def blog_home(request):
    return render(request, "blog/home.html")


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
    return render(request, "blog/dashboard.html", {"name": name.title()})


@require_http_methods(["POST"])
def submit_blog(request):
    if request.method == "POST":
        thumbnail = request.FILES.get("thumbnail")
        title = request.POST.get('title')
        content = request.POST.get('content')  # This contains the HTML from CKEditor
        status = request.POST.get('status')

        print(f"thumbnail: {thumbnail}, title: {title}, content: {content}, status: {status}")
        # Save to your db model 

    return HttpResponse("Submitted....")