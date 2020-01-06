from django.shortcuts import render
from .models import ProductPizza, ProductClassics, ProductSpecials, ProductDrinks


def main(request):
    pizza = ProductPizza.objects.all()
    classics = ProductClassics.objects.all()
    specials = ProductSpecials.objects.all()
    drinks = ProductDrinks.objects.all()
    content = {'ProductPizza': pizza, 'ProductClassics': classics,
               'ProductSpecials': specials, 'ProductDrinks': drinks}


    return render(request, 'pizza/index.html', content)

