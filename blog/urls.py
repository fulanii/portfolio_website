from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap


urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]
