
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('<slug:car_slug>/', views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),
]
