from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ticketing-home'),
    path('tickets/', views.tickets, name='ticketing-tickets'),
]