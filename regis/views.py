from django.shortcuts import render, redirect
from webapp.models import ArticleRequest, Factory, ArticleRequestAnswer, CatalogItem, CatalogItemImage
from webapp.forms import ArticleRequestShowForm, ArticleRequestAnswerForm, ArticleRequestAnswerShowForm, CatalogItemForm
from django.forms import modelformset_factory
from django.db.utils import IntegrityError
from webapp.utils import owr
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
                form_1 = ArticleRequestAnswerShowForm()
                form_1.show(
                    order.get_answer()
                )
                forms.append(form_0.as_table() + form_1.as_table())
            forms = owr(forms)
            return render(request, 'regis/html/menu.html', {'forms': forms})
        if request.method == "POST":
            answer = ArticleRequestAnswer(
                request=ArticleRequest.objects.get(id=request.POST["ArticleRequestId"]),
                amount=request.POST.get('amount')
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
            if form.is_valid():
                new_lot = form.save()
                for image in request.FILES:
                    image = request.FILES[image]
                    CatalogItemImage(CatalogItem=new_lot, image=image).save()
            else:
                return render(request, 'regis/html/create_lot.html', {'form': form})
        form = CatalogItemForm
        return render(request, 'regis/html/create_lot.html', {'form': form})


def edit_lot(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = CatalogItemForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    request.POST['edit_flag']
                except KeyError:
                    form.get_images(CatalogItem.objects.get(id=request.POST['CatalogItem_id']))
                    return render(request, 'regis/html/edit_lot.html', {'form': form})
                try:
                    lot = CatalogItem.objects.get(id=form.data['CatalogItem_id'])
                except CatalogItem.DoesNotExist:
                    return catalog(request, 'Изменить')
                for field in lot._meta.get_fields():
                    if field.name not in ['images', 'id']:
                        setattr(lot, field.name, request.POST[field.name])
                lot.save()
                for key in request.FILES:
                    image = request.FILES[key]
                    if 'swap_image_' in key:
                        CatalogItemImage(id=key.strip('swap_image_'), CatalogItem=lot, image=image).save()
                    else:
                        CatalogItemImage(CatalogItem=lot, image=image).save()
            form.get_images(CatalogItem.objects.get(id=request.POST['CatalogItem_id']))
            return render(request, 'regis/html/edit_lot.html', {'form': form})
        return catalog(request, 'Изменить')


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
