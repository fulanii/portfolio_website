from django.contrib.sitemaps import Sitemap
from .models import Blog  # Import your blog model


class BlogSitemap(Sitemap):
    changefreq = "weekly"  # How frequently the content changes
    priority = 0.8  # Priority for SEO, ranges between 0.0 to 1.0

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return (
            obj.date_posted
        )  # Modify if you use a different field name for the post date
