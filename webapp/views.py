from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ArticleRequest, ArticleRequestForm
from authorisation.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.template import loader
from goldfinger.settings import HOST_URL, STATIC_URL


# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('/authorisation/log_in')
    form = ArticleRequestForm(request.POST)
    if form.is_valid():
        return render(request, 'webapp/html/confirm.html', {'form': form})
    return render(request, 'webapp/html/index.html', {'form': form})


@login_required
def confirm(request):
    form = ArticleRequestForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            order = ArticleRequest(
                profile=UserProfile.objects.get(user=request.user),
                article=form.cleaned_data.get('article'),
                size=form.cleaned_data.get('size'),
                amount=form.cleaned_data.get('amount'),
                factory=form.cleaned_data.get('factory')
            )
            order.save()
            return redirect('/webapp/')
