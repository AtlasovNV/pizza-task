from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import pizza.views as pizza

app_name = 'pizza'

urlpatterns = [
    path('', pizza.main, name='index'),
    path('register/', pizza.RegisterFormView.as_view()),
    path('login/', pizza.LoginFormView.as_view()),
    path('logout/', pizza.LogoutView.as_view()),
]
