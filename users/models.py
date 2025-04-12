from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name='Фамилия'
    )
    email = models.EmailField(
        verbose_name='Электронная почта'
    )
    telephone = models.CharField(
        max_length=20,
        verbose_name='Номер телефона'
    )
    company = models.CharField(
        max_length=255,
        verbose_name='Компания'
    )
    address_1 = models.CharField(
        max_length=255,
        verbose_name='Первый адресс'
    )
    address_2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Второй адресс'
    )
    date_of_birth = models.DateField(
        verbose_name='Дата рождения',
        null=True,
        blank=True
    )
    city = models.CharField(
        max_length=100,
        verbose_name='Город'
    )
    country = models.CharField(
        max_length=100,
        verbose_name='Страна'
    )
    region = models.CharField(
        max_length=100,
        verbose_name='Регион'
    )
    post_code = models.PositiveSmallIntegerField(
        verbose_name='Почтовый код'
    )

