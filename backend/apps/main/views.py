from django.views.generic.base import TemplateView
from django.shortcuts import render
from allauth.account.decorators import verified_email_required


@verified_email_required
def app(request):
    template_name = "app.html"
    return render(request, template_name, {})
