from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("resume/", views.resume, name="resume"),
    path("links/", views.links, name="links"),
    path("blog/", views.temp_blog, name="temp_blog")

]