from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.tryoutsHome, name='tryoutsHome'),

    path('register', views.tryout_register, name='tryout_register'),
    path('tryout_success', views.tryout_success, name='tryout_success'),
    



]  