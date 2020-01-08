from django.db import models

class ProductPizza(models.Model):
    name = models.CharField(verbose_name='Name', max_length=128)
    image = models.ImageField(upload_to='Images', blank=True)
    short_desc = models.CharField(verbose_name='Brief', max_length=60, blank=True)
    description = models.TextField(verbose_name='Description', blank=True)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.name}'

class ProductClassics(models.Model):
    name = models.CharField(verbose_name='Name', max_length=128)
    description = models.TextField(verbose_name='Description', blank=True)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.name}'

class ProductSpecials(models.Model):
    name = models.CharField(verbose_name='Name', max_length=128)
    description = models.TextField(verbose_name='Description', blank=True)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.name}'

class ProductDrinks(models.Model):
    name = models.CharField(verbose_name='Name', max_length=128)
    description = models.TextField(verbose_name='Brief', blank=True)
    price = models.DecimalField(verbose_name='Price', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.name}'

class OrderUser(models.Model):


    name = models.CharField(verbose_name='Order', max_length=128, default='Order')
    nameUser = models.CharField(verbose_name='Name user', max_length=128, default=0)
    email = models.CharField(verbose_name='Email', max_length=128, default=0)
    address = models.CharField(verbose_name='Address', max_length=300, default=0)
    OrderUser = models.CharField(verbose_name='Order User', max_length=300, default=0)
    total = models.DecimalField(verbose_name='Total', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.name}'