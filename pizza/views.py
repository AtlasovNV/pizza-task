from django.shortcuts import render
from .models import ProductPizza, ProductClassics, ProductSpecials, ProductDrinks

from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def main(request):
    pizza = ProductPizza.objects.all()
    classics = ProductClassics.objects.all()
    specials = ProductSpecials.objects.all()
    drinks = ProductDrinks.objects.all()
    content = {'ProductPizza': pizza, 'ProductClassics': classics,
               'ProductSpecials': specials, 'ProductDrinks': drinks}


    return render(request, 'pizza/index.html', content)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "pizza/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "pizza/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")