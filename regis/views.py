from django.shortcuts import render


# Create your views here.
def menu(request):
    if request.user.is_superuser:
        return render(request, 'regis/html/menu.html')
