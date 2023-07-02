import json
from django.contrib.auth.models import User
from authorisation.models import UserProfile
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def read_article_request(request):
    print(json.loads(request.body))
    user = User.objects.get(username='myusername0')
    print(user)
    profile = UserProfile.objects.get(user=user)
    print(profile)
