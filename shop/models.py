from cloudinary.models import CloudinaryField
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Название', max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:shop_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=80, db_index=True)
    slug = models.CharField(max_length=100, db_index=True, unique=True)
    img = CloudinaryField('image')
    description = models.CharField('Описание', max_length=200)
    price = models.IntegerField('Цена')
    size = models.CharField('Размер', max_length=20, db_index=True, default="Euro(200x200)")
    color = models.CharField('Цвет', max_length=100, db_index=True, default="Белый")
    material = models.CharField('Материал', max_length=100, db_index=True, default='Хлопок')
    available = models.BooleanField('Наличие', default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:shop_detail', args=[self.id, self.slug])


