from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ArticleRequest, Factory, JeweleryType, CatalogItem
from .forms import ArticleRequestForm, ArticleRequestShowForm, CatalogItemForm, ArticleRequestAnswerShowForm, CatalogItemImageForm
from authorisation.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.template import loader
from goldfinger.settings import HOST_URL, STATIC_URL
from .utils import owr


# Create your views here.


def make_order(request):
    if not request.user.is_authenticated:
        return redirect('/authorisation/log_in')
    form = ArticleRequestForm(request.POST)
    if form.is_valid():
        form.lock()
        return render(request, 'webapp/html/confirm_order.html', {'form': form})
    return render(request, 'webapp/html/make_order.html', {'form': form})


@login_required
def edit_order(request):
    form = ArticleRequestForm(request.POST)
    return render(request, 'webapp/html/index.html', {'form': form})


@login_required
def confirm_order(request):
    form = ArticleRequestForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            order = ArticleRequest(
                user=request.user,
                article=form.cleaned_data.get('article'),
                size=form.cleaned_data.get('size'),
                amount=form.cleaned_data.get('amount'),
                factory=Factory.objects.all()[int(form.cleaned_data.get('factory'))],
                type=JeweleryType.objects.all()[int(form.cleaned_data.get('type'))]
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
        form_0 = ArticleRequestShowForm()
        form_0.show(order)
        form_0.hide_for_user()
        form_1 = ArticleRequestAnswerShowForm()
        form_1.show(
            order.get_answer()
        )
        forms.append(form_0.as_table() + form_1.as_table())
    forms = owr(forms)
    return render(request, 'webapp/html/request_history.html', {'forms': forms})


@login_required
def catalog(request, button=None):
    if not button:
        button = 'Добавить в корзину'
    forms = []
    for catalogObj in CatalogItem.objects.all():
        form = CatalogItemForm()
        form.show(catalogObj)
        forms.append(form)
    return render(request, 'webapp/html/catalog.html', {'forms': forms, 'button': button})
