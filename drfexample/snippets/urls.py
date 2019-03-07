from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
