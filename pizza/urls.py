from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import pizza.views as portfolio

app_name = 'portfolio'

urlpatterns = [
    path('', portfolio.main, name='index'),
]