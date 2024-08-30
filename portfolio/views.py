from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.conf import settings
from django.contrib.staticfiles import finders

import datetime
import os

from .utils.main import read_data

def index(request):
    context = {
        "year":  datetime.datetime.now().year
    }
    return render(request, "portfolio/home.html", context=context)

def resume(request):
    file_path = finders.find('portfolio/files/resume.pdf')
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')

def links(request):
    context = {
        "url_data": read_data(),
    }
    return render(request, "portfolio/links.html", context)