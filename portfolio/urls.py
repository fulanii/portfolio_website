from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from sitemaps import BlogSitemap, StaticViewSitemap

sitemaps = {
    "blog": BlogSitemap(),
    "static": StaticViewSitemap(),
}



urlpatterns = [
    # path("", views.temp_under_construction, name="home"),
    # path("home/", views.temp_under_construction, name="home"),
    path("", views.index, name="home"),
    path("home/", views.index, name="home"),
    path("resume/", views.resume, name="resume"),
    path("links/", views.links, name="links"),
    path("hire/", views.hire, name="hire"),
    path("download_resume/", views.download_file, name="download_resume"),
    path("contactforms/", views.contact_submit, name="contact_forms"),
    path("robots.txt", views.robots, name="robots"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]