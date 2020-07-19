from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name="index"),
    path('leave_comment', views.leave_comment, name="leave_comment"),
]
