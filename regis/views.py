from django.shortcuts import render
from webapp.models import ArticleOrder
from .models import ArticleRequest


# Create your views here.
def menu(request):
    if request.user.is_superuser:
        forms = []
        for order in ArticleOrder.objects.all():
            form = ArticleRequest()
            form.Meta.model = order
            form.show(order)
            forms.append(form)
        return render(request, 'regis/html/menu.html', {'forms': forms})
