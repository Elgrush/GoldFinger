from .forms import RegistrationForm, EditForm, LoginForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from goldfinger.settings import INVITATION_TOKEN


# Create your views here.
def sign_up(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            if form.cleaned_data.get('token') != INVITATION_TOKEN:
                return render(request, 'authorisation/html/sign_up.html',
                              {'error_message': 'Неверный токен', 'form': form})
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            telephone_number = form.cleaned_data.get('telephone_number')
            if telephone_number[0] != '+':
                telephone_number = '+'+str(int(telephone_number[0]) - 1) + telephone_number[1::]
            profile = UserProfile(user=user, telephone_number=telephone_number,
                                  name=form.cleaned_data.get('name'),
                                  surname=form.cleaned_data.get('surname'),
                                  middle_name=form.cleaned_data.get('middle_name'))
            profile.save()
            return redirect('/webapp/')  # Redirect to the desired page after registration
        else:
            return render(request,
                          'authorisation/html/sign_up.html', {'error_message': 'Неверные данные', 'form': form})
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
                return redirect('/webapp/')
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
    return redirect('/authorisation/log_in/')


@login_required
def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'authorisation/html/profile.html',
                  {
                      'name': profile.name,
                      'surname': profile.surname,
                      'middle_name': profile.middle_name,
                      'phone': profile.telephone_number,
                      'address': profile.address
                  })


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data.get('email')
            telephone_number = form.cleaned_data.get('telephone_number')
            address = form.cleaned_data.get('address')

            if telephone_number[0] != '+':
                telephone_number = '+'+str(int(telephone_number[0]) - 1) + telephone_number[1::]

            user = request.user
            profile = UserProfile.objects.get(user=user)

            profile.telephone_number = telephone_number
            profile.address = address
            profile.name = form.cleaned_data.get('name')
            profile.surname = form.cleaned_data.get('surname')
            profile.middle_name = form.cleaned_data.get('middle_name')
            profile.address = form.cleaned_data.get('address')

            profile.save()

            user.email = email

            user.save()

            return redirect('/authorisation/profile/')
        else:
            return render(request, 'authorisation/html/edit_profile.html',
                          {'form': form,
                           'error_message': 'Неверные данные'})
    form = EditForm({
        'name': UserProfile.objects.get(user=request.user).name,
        'surname': UserProfile.objects.get(user=request.user).surname,
        'middle_name': UserProfile.objects.get(user=request.user).middle_name,
        'username': request.user.username,
        'email': request.user.email,
        'telephone_number': UserProfile.objects.get(user=request.user).telephone_number,
        'address': UserProfile.objects.get(user=request.user).address
    })
    return render(request, 'authorisation/html/edit_profile.html',
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

            return redirect('/authorisation/profile/')
        else:
            return render(request, 'authorisation/html/edit_profile.html',
                          {'form': form,
                           'error_message': 'Неверные данные'})
    form = PasswordChangeForm()
    return render(request, 'authorisation/html/edit_password.html',
                  {'form': form})
