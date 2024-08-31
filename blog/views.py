from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog_home(request):
    return render(request, "blog/home.html")

def blog_login(request):
    return render(request, "blog/login.html")
