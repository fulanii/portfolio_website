from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.
def blog_home(request):
    return render(request, "blog/home.html")

@login_required
def dashboard(request):
    return render(request, "blog/dashboard.html")

def blog_login(request):
    if request.method == "POST":
        username  = request.POST.get('username')
        password  = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('dashboard')) 
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid username or password.'})
        
    return render(request, "blog/login.html")
