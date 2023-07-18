from django.shortcuts import render, redirect
from webapp.models import ArticleRequest, ArticleRequestShowForm, Factory, \
    ArticleRequestAnswer, ArticleRequestAnswerForm, ArticleRequestAnswerShowForm, CatalogItem, CatalogCreationForm
from django.db.utils import IntegrityError
from webapp.utils import owr


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
                forms.append(form_0.as_table()+form_1.as_table())
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
            form = CatalogCreationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            else:
                return render(request, 'regis/html/create_lot.html', {'form': form})
        form = CatalogCreationForm
        return render(request, 'regis/html/create_lot.html', {'form': form})
