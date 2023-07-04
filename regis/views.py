from django.shortcuts import render
from webapp.models import ArticleRequest
from .models import ArticleRequestForm


# Create your views here.
def menu(request):
    if request.user.is_superuser:
        forms = []
        for order in ArticleRequest.objects.all():
            form = ArticleRequestForm()
            form.Meta.model = order
            form.show(order)
            forms.append(form)
        return render(request, 'regis/html/menu.html', {'forms': forms})
