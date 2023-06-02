from django.urls import path, URLResolver

from users.views import LoginView, RegistrationView, LogOutView, ProfileView, ContactsView, SuccessView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('success/', SuccessView.as_view(), name='success'),
]
