from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ArticleRequest, ArticleRequestForm, Factory, ArticleRequestShowForm
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
        form.lock()
        return render(request, 'webapp/html/confirm.html', {'form': form})
    return render(request, 'webapp/html/index.html', {'form': form})


@login_required
def edit_form(request):
    form = ArticleRequestForm(request.POST)
    return render(request, 'webapp/html/index.html', {'form': form})


@login_required
def confirm(request):
    form = ArticleRequestForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            order = ArticleRequest(
                user=request.user,
                article=form.cleaned_data.get('article'),
                size=form.cleaned_data.get('size'),
                amount=form.cleaned_data.get('amount'),
                factory=Factory.objects.all()[int(form.cleaned_data.get('factory'))]
            )
            order.save()
            return redirect('/webapp/')


@login_required
def order_history(request):
    pass


@login_required
def request_history(request):
    forms = []
    for order in ArticleRequest.objects.filter(user=request.user):
        form = ArticleRequestShowForm()
        form.Meta.model = order
        form.show(order)
        form.hide_user()
        forms.append(form)
    return render(request, 'webapp/html/request_history.html', {'forms': forms})
