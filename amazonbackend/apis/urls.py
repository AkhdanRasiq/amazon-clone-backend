from django.urls import path
from . import views, views_product

urlpatterns = [
  path('status', views.LiveChecker.as_view(), name='serverStatus'),
  path('products', views_product.ProductViews.as_view(), name='products')
]
