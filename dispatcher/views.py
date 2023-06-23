import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def read_article_request(request):
    print(json.loads(request.body))
