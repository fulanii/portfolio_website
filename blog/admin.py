from django.contrib import admin
from django.db import models
from django.utils.text import slugify
from tinymce.widgets import TinyMCE
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    
    # Override save_model to ensure slug is generated when saving
    def save_model(self, request, obj, form, change):
        if not obj.slug:  # Only generate slug if it doesn't already exist
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)

admin.site.register(Blog, BlogAdmin)