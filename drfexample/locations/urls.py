from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.LocationList.as_view(), name='location-list'),
    path('<int:pk>/', views.LocationDetail.as_view()),
    path('geolocate/<str:ip_addr>', views.get_location, name='geolocate')
]

urlpatterns = format_suffix_patterns(urlpatterns)
