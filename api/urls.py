from django.contrib import admin
from django.urls import path, include
from .views import hello_view

urlpatterns = [
	path('hello/', hello_view)
]
