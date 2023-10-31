from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('summer_travel/', views.summer_travel, name='summer_travel'),
    path('winter_travel/', views.winter_travel, name='winter_travel'),
    path('test/', views.test, name='test'),
    # path('travel/', views.winter_travel, name='winter_travel'),
    path('travel/<int:travel_id>/', views.travel_detail, name='travel_detail')
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
