from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.events_list, name='events_list'),
    path('<slug:slug>',views.fightCardDetail, name='fightCardDetail'),
    path('<slug:slug>/player/',views.fightCardVideoPlayer, name='fightCardVideoPlayer'),
]  