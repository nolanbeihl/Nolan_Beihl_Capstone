from django.urls import path
from explorers import views

urlpatterns = [
    path('', views.ExplorerList.as_view())
]