from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='first'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('nenad', views.nenad, name='nenad'),
]





"""нету path vk.html"""