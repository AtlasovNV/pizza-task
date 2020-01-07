from django.shortcuts import render
from django.urls import reverse
from .models import ProductPizza, ProductClassics, ProductSpecials, ProductDrinks
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(request):
    pizza = ProductPizza.objects.all()
    classics = ProductClassics.objects.all()
    specials = ProductSpecials.objects.all()
    drinks = ProductDrinks.objects.all()
    content = {'ProductPizza': pizza, 'ProductClassics': classics,
               'ProductSpecials': specials, 'ProductDrinks': drinks}
    return render(request, 'pizza/index.html', content)

def mail(request):
    name = request.POST.get("name")
    adress = request.POST.get("adress")
    sender = request.POST.get("sender")

    user = Mail(
        from_email='Best-pizza@pizza.com',
        to_emails=sender, # Уведомление о заказе пользователю
        subject='Now order pizza - Best pizza!',
        html_content='Hi, ' + name + ' your order pizza. '+ 'Delivery address ' + adress + '. Expect a call to confirm your order! ')
    pizzeria = Mail(
        from_email='Best-pizza@pizza.com',
        to_emails='atlasovnv@yandex.ru', # Уведомление о заказе пиццерии
        subject='Now order pizza - Best pizza!',
        html_content='New order received from ' + name + ' ' + sender + ' ' + adress)
    try:
        sg = SendGridAPIClient('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')
        respons = sg.send(user)
        response = sg.send(pizzeria)
        print(respons.status_code)
        print(respons.body)

        print(response.status_code)
        print(response.body)
    except Exception as e:
        print(str(e))
    return HttpResponseRedirect(reverse('pizza:index'))


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