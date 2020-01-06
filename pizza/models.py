from django.db import models

class ProductPizza(models.Model):
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.name}'

class ProductClassics(models.Model):
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.name}'

class ProductSpecials(models.Model):
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.name}'

class ProductDrinks(models.Model):
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.name}'