from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("login/", views.blog_login, name="blog_login")
]