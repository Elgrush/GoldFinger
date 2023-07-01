from authorisation.models import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from authorisation.models import UserProfile
from goldfinger.settings import HOST_URL


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            telephone_number = form.cleaned_data.get('telephone_number')
            profile = UserProfile(user=user, telephone_number=telephone_number)
            profile.save()
            return redirect(HOST_URL + '/webapp/')  # Redirect to the desired page after registration
        else:
            messages.error(request, "Error")
    else:
        form = RegistrationForm()
        # print(form)
    return render(request, 'authorisation/html/sign_up.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(HOST_URL + '/webapp/')
        else:
            # Handle invalid credentials
            return render(request, 'log_in.html', {'error_message': 'Invalid credentials'})
    elif request.GET.get('telegram_id') is not None:
        try:
            profile = UserProfile.objects.get(telegram_id=request.GET.get('telegram_id'))
            login(username=profile.user.username, password=profile.user.password)
            return redirect(HOST_URL + '/webapp/')
        except UserProfile.DoesNotExist:
            pass
    else:
        # Render the login page for GET request
        return render(request, 'authorisation/html/log_in.html')


def log_out(request):
    logout(request)
    return render(request, 'authorisation/html/log_in.html')
