from authorisation.models import RegistrationForm, EditForm, LoginForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from authorisation.models import UserProfile
from goldfinger.settings import HOST_URL
from django.contrib.auth.decorators import login_required


# Create your views here.
def sign_up(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
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
            return render(request, 'authorisation/html/sign_up.html', {'error_message': 'Неверные данные', 'form': form})
    return render(request, 'authorisation/html/sign_up.html', {'form': form})


def log_in(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(HOST_URL + '/webapp/')
            else:
                # Handle invalid credentials
                return render(request, 'authorisation/html/log_in.html', {
                    "form": form,
                    'error_message': 'Неверные данные'
                })
    return render(request, 'authorisation/html/log_in.html', {
                "form": form
    })


@login_required
def log_out(request):
    logout(request)
    return redirect(HOST_URL + '/authorisation/log_in/')


@login_required
def account(request):
    return render(request, 'authorisation/html/account.html',
                  {'phone': UserProfile.objects.get(user=request.user).telephone_number})


@login_required
def edit_account(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            telephone_number = form.cleaned_data.get('telephone_number')

            user = request.user
            profile = UserProfile.objects.get(user=user)

            profile.telephone_number = telephone_number
            profile.save()

            user.username = username
            user.email = email

            user.save()

            return redirect(HOST_URL + '/authorisation/account/')
        else:
            return render(request, 'authorisation/html/edit_account.html',
                          {'form': form,
                           'error_message': 'Неверные данные'})
    form = EditForm({
        'username': request.user.username,
        'email': request.user.email,
        'telephone_number': UserProfile.objects.get(user=request.user).telephone_number
    })
    return render(request, 'authorisation/html/edit_account.html',
                  {'form': form})

@login_required
def edit_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():

            password = form.cleaned_data.get('password')

            if password != request.user.password:
                return render(request, 'authorisation/html/edit_password.html',
                              {'form': form,
                               'error_message': 'Неверный пароль'})

            password = form.cleaned_data.get('password1')

            if password != form.cleaned_data.get('password2'):
                return render(request, 'authorisation/html/edit_password.html',
                              {'form': form,
                               'error_message': 'Пароли не совпадают'})

            user = request.user

            user.set_password(password)

            user.save()

            return redirect(HOST_URL + '/authorisation/account/')
        else:
            return render(request, 'authorisation/html/edit_account.html',
                          {'form': form,
                           'error_message': 'Неверные данные'})
    form = PasswordChangeForm()
    return render(request, 'authorisation/html/edit_password.html',
                  {'form': form})
