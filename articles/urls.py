from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('article/<slug:slug>',views.article_detail, name='article_detail'),

]  