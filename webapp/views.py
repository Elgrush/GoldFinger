from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from goldfinger.settings import HOST_URL, STATIC_URL
# Create your views here.


def index(request):
    print(request)
    if not request.user.is_authenticated:
        return redirect(HOST_URL+'/authorisation/log_in')
    template = loader.get_template("webapp/html/index.html")
    return HttpResponse(template.render({"MAIN_URL": HOST_URL, "CSS": STATIC_URL}))
