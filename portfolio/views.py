from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
from django.conf import settings
from django.contrib.staticfiles import finders
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.cache import cache_page

import datetime
import os
import requests


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

# def contact_submit(request):
#     if request.method == "POST":
#         data = request.POST

#         # Set default values for subject and message
#         # subject = "New Contact Form Submission"
#         # message = ""

#         # Identify the form and format the email content accordingly
#         if "question" in data:
#             email = data["email"]
#             question = data["question"]
#             subject = "New Question Submitted"
#             message = f"Email: {email}\nQuestion: {question}"

#         elif "company" in data:
#             name = data["name"]
#             email = data["email"]
#             company = data["company"]
#             role = data["role"]
#             subject = "New Recruiter Inquiry"
#             message = f"Name: {name}\nEmail: {email}\nCompany: {company}\nRole: {role}"

#         # elif "services" in data:
#         #     services = data["services"]
#         #     name = data["name"]
#         #     email = data["email"]
#         #     budget = data["budget"]
#         #     due_date = data["due-date"]
#         #     project_description = data["project-description"]
#         #     subject = "Service Inquiry"
#         #     message = (
#         #         f"Service: {services}\nName: {name}\nEmail: {email}\n"
#         #         f"Budget: ${budget}\nDue Date: {due_date}\nDescription: {project_description}"
#         #     )

#         data = {
#             "message": message
#         }

#         response = requests.post("https://hook.us2.make.com/mft0hudwcs8fo7mi2y8o2b5e2dslq937", json=data)

#         if response.status_code == 200:
#             return JsonResponse({"success": True}, status=200)
#         else:
#             return JsonResponse({"success": False, "error": response.text}, status=response.status_code)



def contact_submit(request):
    if request.method == "POST":
        data = request.POST

        # 🔐 Verify reCAPTCHA
        recaptcha_token = data.get("g-recaptcha-response")
        secret_key = "6LfqyXUrAAAAAHDfvZFtByuoeW5-KEfvm7ubRkG6"  # Or use settings.RECAPTCHA_SECRET_KEY

        recaptcha_response = requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={
                "secret": secret_key,
                "response": recaptcha_token,
            }
        )
        result = recaptcha_response.json()

        if not result.get("success"):
            return JsonResponse({"success": False, "error": "reCAPTCHA verification failed."}, status=400)

        # ✅ Continue processing the form
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

        data = {
            "message": message
        }

        response = requests.post("https://hook.us2.make.com/mft0hudwcs8fo7mi2y8o2b5e2dslq937", json=data)

        if response.status_code == 200:
            return JsonResponse({"success": True}, status=200)
        else:
            return JsonResponse({"success": False, "error": response.text}, status=response.status_code)
