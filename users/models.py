from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name='Имя',
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name='Фамилия',
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        null=True,
        blank=True
    )
    telephone = models.CharField(
        max_length=20,
        verbose_name='Номер телефона',
        null=True,
        blank=True
    )
    company = models.CharField(
        max_length=255,
        verbose_name='Компания',
        null=True,
        blank=True
    )
    address_1 = models.CharField(
        max_length=255,
        verbose_name='Первый адрес',
        null=True,
        blank=True
    )
    address_2 = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Второй адрес'
    )
    date_of_birth = models.DateField(
        verbose_name='Дата рождения',
        null=True,
        blank=True
    )
    city = models.CharField(
        max_length=100,
        verbose_name='Город',
        null=True,
        blank=True
    )
    country = models.CharField(
        max_length=100,
        verbose_name='Страна',
        null=True,
        blank=True
    )
    region = models.CharField(
        max_length=100,
        verbose_name='Регион',
        null=True,
        blank=True
    )
    post_code = models.PositiveSmallIntegerField(
        verbose_name='Почтовый код',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} — Профиль"
