from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=80, db_index=True)
    slug = models.CharField(max_length=100, db_index=True, unique=True)
    img = models.ImageField()
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'

    def __str__(self):
        return self.name
