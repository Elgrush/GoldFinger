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
            if str(request.body).count("size") == 2:
                answer = ArticleRequestAnswer(
                    request=ArticleRequest.objects.get(id=request.POST["ArticleRequestId"]),
                    size=request.POST.get('size'),
                    amount=request.POST.get('amount'),
                    factory=Factory.objects.get(id=request.POST["factory"])
                )
                answer.save()
            origform = ArticleRequestShowForm()
            origform.Meta.model = ArticleRequest.objects.get(
                id=request.POST["ArticleRequestId"]
            )
            origform.show(origform.Meta.model)
            form = ArticleRequestAnswerForm()
            form.initial["ArticleRequestId"] = request.POST["ArticleRequestId"]
            return render(request, 'regis/html/answer_request.html', {'origform': origform, 'form': form})
