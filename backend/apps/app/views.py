from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount, SocialToken
from django.shortcuts import render
from apps.profile.models import Profile


@login_required
def react_browse(request):
    return render(request, 'app/app.html')
