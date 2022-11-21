from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.views.decorators.http import condition, last_modified
from django.contrib.auth import get_user_model
import datetime

def latest_update(request, *args, **kwargs):
    print("latest_update")
    return get_user_model().objects.latest('last_login').last_login

# @cache_page(60 * 15)
@last_modified(latest_update)
def index(request):
    date = datetime.datetime.now()
    return HttpResponse(f'{date} - {request.user}')

def test_index(request):
    user = get_user_model().objects.all().values('username',)

    print(user)

    date = datetime.datetime.now()
    return HttpResponse(f'{date} - {request.user} - {user}')