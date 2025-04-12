from django.contrib import admin

from product.models import Product, Review, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

