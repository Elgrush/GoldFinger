from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ArticleRequest, Factory, JeweleryType, CatalogItem, ArticleRequestAnswer
from .forms import ArticleRequestForm, ArticleRequestShowForm, CatalogItemForm, ArticleRequestAnswerForm
from authorisation.models import UserProfile, ShoppingCartOrder, ShoppingCartRequest
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.template import loader
from goldfinger.settings import HOST_URL, STATIC_URL
from .utils import owr


@login_required
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
                factory=Factory.objects.get(id=int(form.data['factory'])),
                type=JeweleryType.objects.get(id=int(form.data['type'])),
            )
            order.save()
            return redirect('/webapp/')


@login_required
def order_history(request):
    pass


@login_required
def request_history(request):
    if request.method == 'POST':
        ArticleRequest.objects.get(id=request.POST['id']).delete()
        return redirect('/webapp/')
    forms = []
    for order in ArticleRequest.objects.filter(user=request.user):
        form_0 = ArticleRequestShowForm()
        form_0.show(order)
        form_0.hide_for_user()
        form_1 = ArticleRequestAnswerForm()
        form_1.show(
            order.get_answer()
        )
        forms.append(form_0.as_table() + form_1.as_table())
    forms = owr(forms)
    return render(request, 'webapp/html/request_history.html', {'forms': forms})


@login_required
def catalog(request, button=None, action=None):
    objects = []
    for catalogObj in CatalogItem.objects.order_by('-updated_at')[:20]:
        objects.append({
            'id': catalogObj.id,
            'article': catalogObj.article,
            'size': catalogObj.size,
            'amount': catalogObj.amount,
            'price': catalogObj.price,
            'factory': catalogObj.factory,
            'type': catalogObj.type,
            'images': catalogObj.get_images()
        })
    return render(request, 'webapp/html/catalog.html', {'objects': objects, 'button': button, 'action': action})


@login_required
def add_item_to_cart(request):
    try:
        ShoppingCartOrder.objects.get(UserProfile=UserProfile.objects.get(user=request.user),
                                      CatalogItem=CatalogItem.objects.get(
                                          id=request.POST['id']))
        response = HttpResponse(headers={"success": 0})
        return response
    except ObjectDoesNotExist:
        if 'amount' in request.POST.keys():
            amount = int(request.POST['amount'])
            lot = CatalogItem.objects.get(id=request.POST['id'])
            if amount > lot.amount or amount > 0:
                amount = lot.amount
            ShoppingCartOrder(UserProfile=UserProfile.objects.get(user=request.user),
                              CatalogItem=lot, amount=amount).save()
        else:
            ShoppingCartOrder(UserProfile=UserProfile.objects.get(user=request.user),
                              CatalogItem=CatalogItem.objects.get(
                                  id=request.POST['id']), amount=0).save()
        response = HttpResponse(headers={"success": 1})
        return response
    except MultipleObjectsReturned:
        response = HttpResponse(headers={"success": 1})
        return response


@login_required
def shopping_cart(request):
    lot_forms = []
    for CartItem in UserProfile.objects.get(user=request.user).get_catalog_cart():
        form = CatalogItemForm()
        form.show(CartItem.CatalogItem)
        form.amount_bought = CartItem.amount
        lot_forms.append(form)
    request_forms = []
    for CartItem in UserProfile.objects.get(user=request.user).get_request_cart():
        form = CatalogItemForm()
        form.show(CartItem.ArticleRequestAnswer.request)
        form.initial['CatalogItem_id'] = CartItem.ArticleRequestAnswer.id
        form.initial['amount'] = CartItem.ArticleRequestAnswer.amount
        form.initial['price'] = CartItem.ArticleRequestAnswer.price
        form.amount_bought = CartItem.amount
        request_forms.append(form)
    return render(request, 'webapp/html/cart.html', {'lot_forms': lot_forms, 'request_forms': request_forms})


@login_required
def discard_item_from_cart(request):
    try:
        ShoppingCartOrder.objects.get(UserProfile=UserProfile.objects.get(user=request.user), CatalogItem=CatalogItem.
                                      objects.get(id=request.POST['id'])).delete()
        response = HttpResponse(headers={"success": 1})
        return response
    except ObjectDoesNotExist:
        response = HttpResponse(headers={"success": 0})
        return response
    except MultipleObjectsReturned:
        ShoppingCartOrder.objects.filter(UserProfile=UserProfile.objects.get(user=request.user),
                                         CatalogItem=CatalogItem.
                                         objects.get(id=request.POST['id'])).delete()
        response = HttpResponse(headers={"success": 1})
        return response


@login_required
def discard_request_from_cart(request):
    try:
        ShoppingCartRequest.objects.get(UserProfile=UserProfile.objects.get(user=request.user), ArticleRequestAnswer=
                                        ArticleRequestAnswer.objects.get(id=request.POST['id'])).delete()
        response = HttpResponse(headers={"success": 1})
        return response
    except ObjectDoesNotExist:
        print(request.POST['id'])
        response = HttpResponse(headers={"success": 0})
        return response
    except MultipleObjectsReturned:
        ShoppingCartRequest.objects.filter(UserProfile=UserProfile.objects.get(user=request.user),
                                           ArticleRequestAnswer=ArticleRequestAnswer.
                                           objects.get(id=request.POST['id'])).delete()
        response = HttpResponse(headers={"success": 1})
        return response


@login_required
def set_cart_amount(request):
    try:
        order = ShoppingCartOrder.objects.get(UserProfile=UserProfile.objects.get(user=request.user),
                                              CatalogItem=CatalogItem.objects.get(
                                                  id=request.POST['id']))
        amount = int(request.POST['amount'])
        if amount > order.CatalogItem.amount or amount > 0:
            amount = order.CatalogItem.amount
        order.amount = amount
        order.save()
        response = HttpResponse(headers={"success": 1})
        return response
    except ObjectDoesNotExist:
        response = HttpResponse(headers={"success": 0})
        return response


@login_required
def add_request_to_cart(request):
    try:
        ShoppingCartRequest.objects.get(UserProfile=UserProfile.objects.get(user=request.user),
                                        ArticleRequestAnswer=ArticleRequestAnswer.objects.get(
                                            id=request.POST['id']))
        response = HttpResponse(headers={"success": 0})
        return response
    except ObjectDoesNotExist:
        shopping_request = ShoppingCartRequest(UserProfile=UserProfile.objects.get(user=request.user),
                                               ArticleRequestAnswer=ArticleRequestAnswer.objects.get(
                                                   id=request.POST['id']), amount=0)
        if shopping_request.ArticleRequestAnswer.request.amount <= shopping_request.ArticleRequestAnswer.amount:
            shopping_request.amount = shopping_request.ArticleRequestAnswer.request.amount
        else:
            shopping_request.amount = shopping_request.ArticleRequestAnswer.amount
        shopping_request.save()
        response = HttpResponse(headers={"success": 1})
        return response
    except MultipleObjectsReturned:
        response = HttpResponse(headers={"success": 1})
        return response
    except ValueError:
        response = HttpResponse(headers={"success": -1})
        return response
