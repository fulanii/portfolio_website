from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
from django.conf import settings
from django.contrib.staticfiles import finders
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.cache import cache_page

import datetime
import os

from .utils.main import read_data

@cache_page(60 * 15)  # Cache for 15 minutes
def index(request):
    context = {
        "year": datetime.datetime.now().year,
    }

    return render(request, "portfolio/home.html", context=context)

def robots(request):
   return render(request, "robots.txt")

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

        # Set default values for subject and message
        # subject = "New Contact Form Submission"
        # message = ""

        # Identify the form and format the email content accordingly
        if "question" in data:
            email = data["email"]
            question = data["question"]
            subject = "New Question Submitted"
            message = f"Email: {email}\nQuestion: {question}"

        elif "company" in data:
            name = data["name"]
            email = data["email"]
            company = data["company"]
            role = data["role"]
            subject = "New Recruiter Inquiry"
            message = f"Name: {name}\nEmail: {email}\nCompany: {company}\nRole: {role}"

        elif "services" in data:
            services = data["services"]
            name = data["name"]
            email = data["email"]
            budget = data["budget"]
            due_date = data["due-date"]
            project_description = data["project-description"]
            subject = "Service Inquiry"
            message = (
                f"Service: {services}\nName: {name}\nEmail: {email}\n"
                f"Budget: ${budget}\nDue Date: {due_date}\nDescription: {project_description}"
            )

        # Send the email
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # From email (the one you set in settings)
            [
                "yassine@yassinecodes.dev" # Recipient's email address (replace with the desired recipient)
            ],  
            fail_silently=False,
        )

        # Respond with success
        return JsonResponse({"success": True})

    return JsonResponse(
        {"success": False, "error": "Invalid request method"}, status=400
    )
