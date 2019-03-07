from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.SnippetList.as_view(), name='snippet-list'),
    path('<int:pk>', views.SnippetDetail.as_view()),
    path('snippet/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
