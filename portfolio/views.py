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


# --------------------------------------- temp under contruction ----------------------------------------------
import requests
import logging
from django.shortcuts import render
from django.utils import timezone
from user_agents import parse

# Configuration
logger = logging.getLogger(__name__)
WEBHOOK_URL = "https://hook.us2.make.com/huw0otphtdaohayampvt301xpqilxy7n" 
IP_API_URL = "http://ip-api.com/json/{ip}"


def get_client_ip(request):
    """Retrieves the client's IP address, prioritizing X-Forwarded-For."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    # This return statement was missing/misplaced, causing the function to return None in production.
    return ip


def get_ip_location_data(ip_address):
    """Performs an API call to get ALL location data for the IP address."""
    try:
        url = IP_API_URL.format(ip=ip_address)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        data = response.json()

        if data.get('status') == 'success':
            return data
        else:
            return {"status": f"IP-API Error: {data.get('message', 'Unknown failure')}", "query": ip_address}

    except requests.exceptions.RequestException as e:
        logger.error(f"IP-API request error for IP {ip_address}: {e}")
        return {"status": f"Network Error: {e}", "query": ip_address}


def send_webhook_data(data):
    """Sends the collected visitor data as JSON to the webhook URL (Synchronous)."""
    try:
        response = requests.post(WEBHOOK_URL, json=data, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to send visitor data to webhook: {e}")


def temp_under_construction(request):
    """Captures visitor data, sends it to the webhook synchronously, and renders the page."""
    ip_address = get_client_ip(request)
    user_agent_string = request.META.get('HTTP_USER_AGENT', 'Unknown')
    user_agent = parse(user_agent_string)
    
    # Get the full IP-API JSON response
    ip_api_response = get_ip_location_data(ip_address)

    # Gather Data
    data_to_send = {
        "timestamp": timezone.now().isoformat(),
        # This will now correctly contain the client's IP address
        "client_ip": ip_address, 
        "request_details": {
            "method": request.method,
            "path": request.path,
            "is_secure": request.is_secure(),
        },
        "device_info": {
            "browser": user_agent.browser.family,
            "os": user_agent.os.family,
            "device_type": (
                "mobile" if user_agent.is_mobile
                else ("tablet" if user_agent.is_tablet else "desktop")
            ),
            "is_bot": user_agent.is_bot,
            "user_agent_raw": user_agent_string,
        },
        "ip_lookup_data": ip_api_response,
        "key_headers": {
            "referrer": request.META.get('HTTP_REFERER', 'N/A'),
            "accept_language": request.META.get('HTTP_ACCEPT_LANGUAGE', 'N/A'),
        }
    }

    # Send Data Synchronously
    send_webhook_data(data_to_send)

    # Render Page (Immediate Response)
    return render(request, "portfolio/temp.html")
# --------------------------------------- temp under contruction ----------------------------------------------


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
