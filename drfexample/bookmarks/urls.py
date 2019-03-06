from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.BookmarkList.as_view(), name='bookmark-list'),
    path('<int:pk>', views.BookmarkDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
