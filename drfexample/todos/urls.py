from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.ToDoList.as_view(), name='todo-list'),
    path('<int:pk>', views.ToDoDetail.as_view(), name='todo-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
