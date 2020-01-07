from django.urls import path
import pizza.views as pizza

app_name = 'pizza'

urlpatterns = [
    path('', pizza.main, name='index'),
    path('mail/', pizza.mail),
    path('register/', pizza.RegisterFormView.as_view()),
    path('login/', pizza.LoginFormView.as_view()),
    path('logout/', pizza.LogoutView.as_view()),
]
