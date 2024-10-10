from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("login/", views.blog_login, name="login"),
    path("logout/", views.blog_logout, name="logout"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]