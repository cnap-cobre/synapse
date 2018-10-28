from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

@login_required
def add_beocat_script(request, template_name='add_beocat_script.html'):
    session_key = request.COOKIES[settings.SESSION_COOKIE_NAME]
    csrf = request.COOKIES['csrftoken']
    return render(request, template_name, {
        'sessionkey': session_key,
        'csrftoken': csrf
    }, content_type='text/plain')