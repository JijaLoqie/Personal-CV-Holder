from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
	path('home/', index),
	path('create/', index),
	path('update/', index),
	path('home/cv/<str:code>/', index),
]
