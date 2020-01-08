from django.urls import path
import pizza.views as pizza
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pizza'

urlpatterns = [
    path('', pizza.main, name='index'),
    path('order/', pizza.order),
    path('register/', pizza.RegisterFormView.as_view()),
    path('login/', pizza.LoginFormView.as_view()),
    path('logout/', pizza.LogoutView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

