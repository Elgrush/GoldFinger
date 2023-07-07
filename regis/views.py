from django.shortcuts import render
from webapp.models import ArticleRequest, ArticleRequestShowForm, Factory
from.models import ArticleRequestAnswer, ArticleRequestAnswerForm
from django.contrib.auth.models import User


# Create your views here.
def menu(request):
    if request.user.is_superuser:
        forms = []
        for order in ArticleRequest.objects.all():
            form = ArticleRequestShowForm()
            form.Meta.model = order
            form.show(order)
            forms.append(form)
        return render(request, 'regis/html/menu.html', {'forms': forms})


def answer_request(request):
    if request.user.is_superuser:
        if request.method == "POST":
            origform = ArticleRequestShowForm()
            origform.Meta.model = ArticleRequest.objects.get(
                user=User.objects.get(username=request.POST["user"]),
                article=request.POST["article"],
                size=request.POST["size"],
                amount=request.POST["amount"],
                factory=Factory.objects.get(name=request.POST["factory"])
            )
            origform.show(origform.Meta.model)
            form = ArticleRequestAnswerForm()
            form.Meta.model =
            return render(request, 'regis/html/answer_request.html', {'origform': origform})
