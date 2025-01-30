from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Blog  # Import only necessary models

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.date_posted

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = "monthly"

    def items(self):
        return ["home", "hire", "links", "resume", "download_resume", ]

    def location(self, item):
        return reverse(item)
