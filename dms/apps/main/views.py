from django.views.generic.base import TemplateView
from django.shortcuts import render
from allauth.account.decorators import verified_email_required

@verified_email_required
def home_page(request):
    template_name = "home.html"
    return render(request, template_name, {})

