from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo, name='demo'),
    path('newinteraction/', views.new_interaction, name='new_interaction'),
]
