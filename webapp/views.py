from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from goldfinger.settings import HOST_URL, STATIC_URL
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('/authorisation/log_in')
    return render(request, 'webapp/html/index.html')
