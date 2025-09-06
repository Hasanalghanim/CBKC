from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import TryoutEventList,TryoutRegistrantList,TryoutEventDetail

urlpatterns = [
    path('', views.tryoutsHome, name='tryoutsHome'),

    path('register', views.tryout_register, name='tryout_register'),
    path('tryout_success', views.tryout_success, name='tryout_success'),


    path('api/TryoutEventList', TryoutEventList.as_view(), name='TryoutEventList'),
    path('api/TryoutRegistrantList/<int:tryout_event_id>/', TryoutRegistrantList.as_view(), name='TryoutRegistrantList'),
    path('api/tryout/<slug:slug>/', TryoutEventDetail.as_view(), name='tryout-event-detail'),

    
]  