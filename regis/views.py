from django.shortcuts import render
from webapp.models import ArticleOrder
from .models import ArticleRequest


# Create your views here.
def menu(request):
    if request.user.is_superuser:
        forms = []
        for order in ArticleOrder.objects.all():
            a = ArticleRequest(order)
            print(a)
            forms.append(a)
        print(forms)
        return render(request, 'regis/html/menu.html')
