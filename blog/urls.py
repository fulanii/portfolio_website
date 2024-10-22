from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogSitemap  

sitemaps = {
    'blog': BlogSitemap,  
}

urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("googled207b771908af026.html/", views.google_console, name="google_console")
]