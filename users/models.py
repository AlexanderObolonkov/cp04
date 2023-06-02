from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    patronymic = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)

    def __str__(self):
        if self.is_superuser:
            role = 'админ'
        elif self.is_staff:
            role = 'сотрудник'
        else:
            role = 'пользователь'
        return f'{role} {self.first_name} {self.last_name} {self.patronymic} "{self.username}"'
