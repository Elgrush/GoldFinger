from django.http import HttpResponse
from django.template import loader
from goldfinger.settings import HOST_URL
# Create your views here.


def index(request):
    template = loader.get_template("webapps/index.html")
    return HttpResponse(template.render({"MAIN_URL": HOST_URL}))
