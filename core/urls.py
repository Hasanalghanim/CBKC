from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', include('fightCards.urls') ),
    path('tryouts/', include('tryouts.urls') ),
    path('dashboard/', include('dashboard.urls') ),
    path('fighters/', include('fighters.urls') ),
    path('articles/', include('articles.urls') ),
    path('ckeditor/', include('ckeditor_uploader.urls')),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)