from django.urls import path
from . import views


# django naming convention
urlpatterns = [
    path('', views.index),
    path('new', views.new_products)
]