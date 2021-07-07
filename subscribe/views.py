from django.core.checks import messages
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.conf import settings
from .forms import EmailSubscribeForm
from .models import Subscribe

import json
import requests

# Create your views here.

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID


api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0/'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'


def subscribe(email):
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    r = requests.post(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()


def email_list_signup(request):
    form = EmailSubscribeForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email_subscribe_qs = Subscribe.objects.filter(
                email=form.instance.email)
            if email_subscribe_qs.exists():
                messages.info(request, "You are already subscribed")
            else:
                subscribe(form.instance.email)
                form.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def index(request):
    form = EmailSubscribeForm()
    if request.method == "POST":
        email = request.POST["email"]
        new_subscribe = Subscribe()
        new_subscribe.email = email
        new_subscribe.save()

    context = {
        'form': form
    }
    return render(request, 'subscribe/index.html', context)
