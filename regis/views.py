from django.shortcuts import render, redirect, HttpResponse
from webapp.models import ArticleRequest, Factory, ArticleRequestAnswer, CatalogItem, CatalogItemImage, JeweleryType
from webapp.forms import ArticleRequestShowForm, ArticleRequestAnswerForm, CatalogItemForm
from django.db.utils import IntegrityError
from webapp.utils import owr
from regis.sokolov_parser import request_article
from webapp.views import catalog


# Create your views here.
def menu(request):
    if request.user.is_superuser:
        if request.method == "GET":
            forms = []
            for order in ArticleRequest.objects.all():
                form_0 = ArticleRequestShowForm()
                form_0.Meta.model = order
                form_0.show(order)
                form_0.hide_user()
                form_1 = ArticleRequestAnswerForm()
                form_1.show(
                    order.get_answer()
                )
                forms.append(form_0.as_table() + form_1.as_table())
            forms = owr(forms)
            return render(request, 'regis/html/menu.html', {'forms': forms})
        if request.method == "POST":
            answer = ArticleRequestAnswer(
                request=ArticleRequest.objects.get(id=request.POST["ArticleRequestId"]),
                amount=request.POST.get('amount'), price=request.POST.get('price')
            )
            try:
                answer.save()
            except IntegrityError:
                ArticleRequestAnswer.objects.get(
                    request=ArticleRequest.objects.get(id=request.POST["ArticleRequestId"])).delete()
                answer.save()
        return redirect("/regis/")


def create_lot(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = CatalogItemForm(request.POST, request.FILES)
            new_lot = CatalogItem(
                article=form.data['article'],
                size=form.data['size'],
                amount=form.data['amount'],
                factory=Factory.objects.get(id=int(form.data['factory'])),
                type=JeweleryType.objects.get(id=int(form.data['type'])),
                price=form.data['price']
            )
            new_lot.save()
            for image in request.FILES:
                image = request.FILES[image]
                CatalogItemImage(CatalogItem=new_lot, image=image).save()
        form = CatalogItemForm
        return render(request, 'regis/html/create_lot.html', {'form': form})


def edit_lot(request):
    if request.user.is_superuser:
        if request.method == "POST":
            try:
                request.POST._mutable = True
                request.POST['factory'] = Factory.objects.get(id=request.POST['factory'])
                request.POST['type'] = JeweleryType.objects.get(id=request.POST['type'])
                request.POST._mutable = False
            except ValueError:
                request.POST['factory'] = Factory.objects.get(name=request.POST['factory'])
                request.POST['type'] = JeweleryType.objects.get(name=request.POST['type'])
                request.POST._mutable = False
            form = CatalogItemForm(request.POST, request.FILES)
            if form.is_valid() or all(
                    [x in request.POST.keys() for x in [
                        'article', 'amount', 'price', 'CatalogItem_id', 'factory', 'type']]):
                try:
                    request.POST['edit_flag']
                except KeyError:
                    form.get_images(CatalogItem.objects.get(id=request.POST['CatalogItem_id']))
                    return render(request, 'regis/html/edit_lot.html', {'form': form})
                try:
                    lot = CatalogItem.objects.get(id=form.data['CatalogItem_id'])
                except CatalogItem.DoesNotExist:
                    return catalog(request, 'Изменить лот', 'submit')
                item = CatalogItem.objects.get(id=request.POST['CatalogItem_id'])
                item.article = request.POST['article']
                item.size = request.POST['size']
                item.price = request.POST['price']
                item.factory = request.POST['factory']
                item.type = request.POST['type']
                item.save()
                for key in request.FILES:
                    image = request.FILES[key]
                    if 'swap_image_' in key:
                        CatalogItemImage(id=key.strip('swap_image_'), CatalogItem=lot, image=image).save()
                    else:
                        CatalogItemImage(CatalogItem=lot, image=image).save()
            form.get_images(CatalogItem.objects.get(id=request.POST['CatalogItem_id']))
            return render(request, 'regis/html/edit_lot.html', {'form': form})
        return catalog(request, 'Изменить лот', 'submit')


def delete_image(request):
    if request.user.is_superuser:
        if request.method == "POST":
            CatalogItemImage.objects.get(id=request.POST['id']).delete()
        return redirect("/regis/")


def delete_lot(request):
    if request.user.is_superuser:
        if request.method == "POST":
            CatalogItem.objects.get(id=request.POST['CatalogItem_id']).delete()
            return redirect("/regis/")
        return catalog(request, 'Удалить')


def parse(request):
    return render(request, 'regis/html/parse.html')


def parser(request):
    data = request_article(request.POST['article'])
    return HttpResponse(headers={"data": data})
