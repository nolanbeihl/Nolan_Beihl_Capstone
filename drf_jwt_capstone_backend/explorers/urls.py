from django.urls import path
from explorers import views

urlpatterns = [
    path('', views.create_explorer),
    path('', views.explorer_info),
]