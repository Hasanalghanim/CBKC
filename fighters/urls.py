from django.urls import path
from . import views


urlpatterns = [
    path('all', views.allFighters, name='allFighters'),
    path('fighter/<slug:slug>',views.fighter_detail, name='fighter_detail'),
]  