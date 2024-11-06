from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
from django.conf import settings
from django.contrib.staticfiles import finders
from django.contrib import messages

import datetime
import os

from .utils.main import read_data


def index(request):
    context = {
        "year": datetime.datetime.now().year,
    }

    return render(request, "portfolio/home.html", context=context)


def resume(request):
    file_path = finders.find("portfolio/files/resume.pdf")
    return FileResponse(open(file_path, "rb"), content_type="application/pdf")
    # return render(request, "portfolio/coming_soon.html")


def links(request):
    context = {
        "url_data": read_data(),
    }
    return render(request, "portfolio/links.html", context)


def hire(request):
    # return render(request, "portfolio/hire.html")
    return render(request, "portfolio/hire.html")


def download_file(request, filename="yassinecodes_resume.pdf"):
    # Define the path to your file, replace with your file's actual path
    file_path = finders.find("portfolio/files/resume.pdf")

    response = FileResponse(open(file_path, "rb"))
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


def contact_submit(request):
    if request.method == "POST":
        data = request.POST
        if "question" in data:
            email = data["email"]
            question = data["question"]

        elif "company" in data:
            name = data["name"]
            email = data["email"]
            company = data["company"]
            role = data["role"]

        elif "services" in data:
            services = data["services"]
            name = data["name"]
            email = data["email"]
            budget = data["budget"]
            due_date = data["due-date"]
            project_descption = data["project-description"]

        # next send email using form data

        return JsonResponse({"success": True})
