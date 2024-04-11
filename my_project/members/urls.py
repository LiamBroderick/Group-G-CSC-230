from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('exhibits_page/', views.exhibits_page, name='exhibits_page'),
    path('science_of_play/', views.science_of_play, name='science_of_play'),
    path('map/', views.map, name='map'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
