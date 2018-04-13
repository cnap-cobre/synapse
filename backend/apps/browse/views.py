from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount, SocialToken
from django.shortcuts import render
from agavepy.agave import Agave, Token

@login_required
def browse_beocat_home(request):
    user = request.user
    try:
        sa = SocialAccount.objects.filter(user=user, provider='agave').get()
        try:
            st = SocialToken.objects.filter(account=sa).get().token
            ag = Agave(token=st,
                    api_server='https://public.agaveapi.co')
            files = ag.files.list(filePath='', systemId='beocat', limit=250, offset=0)
        except SocialToken.DoesNotExist:
            files = []
    except SocialAccount.DoesNotExist:
        files = []
    return render(request, 'browse/browse.html', {'files': files})

@login_required
def react_browse(request):
    return render(request, 'browse/react-browse.html', {})
