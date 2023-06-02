from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2', 'placeholder': 'Введите логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2', 'placeholder': 'Введите фамилию'}))
    patronymic = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2', 'placeholder': 'Введите отчество (опцианально)'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-2', 'placeholder': 'Введите адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'patronymic', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-2'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-2'}))
    patronymic = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-2'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-2', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-2', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'patronymic', 'username', 'email')


class FeedBackForm(forms.Form):
    """Класс формы обратной связи"""
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'placeholder': "Ваше имя"
    }))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'placeholder': "Ваша почта"
    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'subject',
        'placeholder': "Тема"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control md-textarea',
        'id': 'message',
        'rows': 3,
        'placeholder': "Ваше сообщение"
    }))
