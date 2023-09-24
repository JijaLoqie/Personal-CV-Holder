from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
	path('get-resumes', ResumeView.as_view()),
	path('get-resume', GetResumeView.as_view()),
	path('create-resume', CreateResumeView.as_view()),
	path('update-resume', hello_view),
]
