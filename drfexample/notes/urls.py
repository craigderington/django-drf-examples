from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list),
    path('<int:note_pk_id>/', views.note_detail),
]