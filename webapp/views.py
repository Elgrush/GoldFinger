from django.http import HttpResponse
from django.template import loader
from goldfinger.settings import HOST_URL, STATIC_URL
# Create your views here.


def index(request):
    template = loader.get_template("webapp/html/index.html")
    return HttpResponse(template.render({"MAIN_URL": HOST_URL, "CSS": STATIC_URL}))
