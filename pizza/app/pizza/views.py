from django.shortcuts import render
from django.urls import reverse
from .models import ProductPizza, ProductClassics, ProductSpecials, ProductDrinks, OrderUser
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

def order(request):
    order = OrderUser.objects.all()

    name = request.POST.get("name")
    adress = request.POST.get("adress")
    sender = request.POST.get("sender")
    subTotalPrice = request.POST.get("subTotalPrice")
    totalCoutn = request.POST.get("totalCount")
    total = request.POST.get("total")

    receipt = []
    for i in range(20):
        item_name_ = "item_name_" + str(i)
        itemPriceText_ = "itemPriceText_" + str(i)
        itemCount_ = "itemCount_" + str(i)
        productName = request.POST.get(item_name_)
        productPrice = request.POST.get(itemPriceText_)
        productCount = request.POST.get(itemCount_)
        if productName != None:
            receipt.append(productName)
        if productPrice != None:
            receipt.append(productPrice)
        if productCount != None:
            receipt.append(productCount)
    receipt = ' '.join(receipt)

    a = OrderUser.objects.create(OrderUser=receipt, nameUser=name, email=sender, address=adress, total=total)
    a.save()

    orderUser = (
            'Your last order in name ' + name + '. ' + receipt + ' ' + ' Delivery address ' + adress +
            '. Email ' + sender + '. Intermediate cost - ' + subTotalPrice + '$' + '. Quantity - ' + totalCoutn
            + '. Total cost with delivery - ' + total + '$')

    orderPizzeri = ('New order from ' + name + ' address delivery ' + adress + ' ' +sender + '. Order list: '
                    + receipt + ' quantity. ' + total + '$')

    user = Mail(
                from_email='valerjevitchnicolas@yandex.ru',
                to_emails=sender, # Уведомление пользователю
                subject='Now order pizza - Best pizza!',
                html_content= orderUser)
    pizzeria = Mail(
                from_email='Best-pizza@pizza.com',
                to_emails='valerjevitchnicolas@yandex.ru', # Уведомление владельца
                subject='Now order pizza - Best pizza!',
                html_content=orderPizzeri)
    try:
        sg = SendGridAPIClient('API_KEY')
        respons = sg.send(user)
        response = sg.send(pizzeria)
        print(respons.status_code)
        print(respons.body)
        print(response.status_code)
        print(response.body)
    except Exception as e:
        print(str(e))

    content = {'OrderUser': order}
    return HttpResponseRedirect(reverse('pizza:index'), content)

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
