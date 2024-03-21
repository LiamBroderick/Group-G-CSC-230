from django.urls import path
from . import views
from .views import museum_page

urlpatterns = [
    path('museum_page/', views.museum_page, name='museum_page'),
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]