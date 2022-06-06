from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_show', 'slug', 'price', 'available']
    list_filter = ['available', 'price']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    def image_show(self, obj):
        if obj.img:
            return mark_safe("<img src='{}' width='40' />".format(obj.img.url))
        return "None"