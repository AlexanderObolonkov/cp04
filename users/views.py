from os import getenv

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth, messages
from django.views import View
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, FeedBackForm


class LoginView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = UserLoginForm()
        return render(
            request,
            'users/login.html',
            context={
                'navbar': 'login',
                'form': form,
            }
        )

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        return render(
            request,
            'users/login.html',
            context={
                'navbar': 'login',
                'form': form,
            }
        )


class RegistrationView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = UserRegistrationForm()
        return render(
            request,
            'users/registration.html',
            context={
                'navbar': 'registration',
                'form': form,
            }
        )

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешная регистрация!')
            return HttpResponseRedirect(reverse('users:login'))
        return render(
            request,
            'users/registration.html',
            context={
                'navbar': 'registration',
                'form': form,
            }
        )


class ProfileView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = UserRegistrationForm(instance=request.user)
        return render(
            request,
            'users/profile.html',
            context={
                'navbar': 'account',
                'form': form,
            }
        )

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        return render(
            request,
            'users/profile.html',
            context={
                'navbar': 'account',
                'form': form,
            }
        )


class LogOutView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))


class ContactsView(View):
    """View страницы контактов"""

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для станицы контактов"""
        form = FeedBackForm()
        return render(request, 'users/contacts.html', context={
            'nav_bar': 'contacts',
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """POST-запрос для страницы контактов"""
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            mail = getenv('MAIN_EMAIL') or ''
            try:
                send_mail(f'От {name} | {from_email} | {subject}', message, from_email, [mail])
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect(reverse('users:success'))
        return render(request, 'users/contacts.html', context={
            'form': form,
        })


class SuccessView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для страницы успеха"""
        return render(request, 'users/success.html', context={
            'title': 'Спасибо'
        })
