from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("googled207b771908af026.html/", views.google_console, name="google_console")
]