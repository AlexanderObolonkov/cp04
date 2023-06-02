from django.db.models.query import QuerySet

from users.models import User
from antique.models import Client, Employee


def get_from_db(user: User):
    if user.is_staff:
        return _get_employee_by_user(user)
    return _get_client_by_user(user)


def _get_client_by_user(user: User):
    return Client.objects.filter(email=user.email)


def _get_employee_by_user(user: User):
    return Employee.objects.filter(phone_number=user.phone_number)
