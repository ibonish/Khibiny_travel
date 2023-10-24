from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('travel', views.travel, name='travel'),
    path('teriberka', views.teriberka, name='teriberka'),
    path('white_sea', views.white_sea, name='white_sea'),
    path('khibiny_heart', views.khibiny_heart, name='khibiny_heart'),
    path('polar_shine', views.polar_shine, name='polar_shine'),
    path('snow_travel', views.snow_travel, name='snow_travel'),
    path('white_sea', views.white_sea, name='white_sea'),
    path('snow_walk', views.snow_walk, name='snow_walk'),
    path('walk', views.walk, name='walk'),
    path('seidozero', views.seidozero, name='seidozero'),
    path('art_park', views.art_park, name='art_park'),
    path('etno', views.etno, name='etno'),
] 