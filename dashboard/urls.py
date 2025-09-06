from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import  check_auth, logout_view,login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('api/check-auth/', check_auth, name='check-auth'),
    path('api/logout/', logout_view, name='logout'),
    path('api/login/', login_view, name='login'),

]  