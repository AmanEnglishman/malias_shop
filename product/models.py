from datetime import timedelta
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='products/',
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )
    discount = models.PositiveIntegerField(
        verbose_name='Скидка',
        blank=True,
        null=True
    )
    discount_amount = models.PositiveIntegerField(
        verbose_name='Сумма скидки',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.title} - {self.price} $'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    @property
    def average_rating(self):
        return self.reviews.aggregate(avg=models.Avg('rating'))['avg'] or 0

    def is_new(self):
        created_at_dt = self.created_at
        if isinstance(created_at_dt, str):
            created_at_dt = parse_datetime(created_at_dt)
        return timezone.now() - created_at_dt <= timedelta(days=7)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(choices=[(i, f"{i} звезд") for i in range(6)], verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user')  # Один пользователь может оставить только одну оценку на продукт
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.user} — {self.product} — {self.rating}★"
