from django.urls import path
from . import views

urlpatterns = [
  path('status', views.LiveChecker.as_view())
]
