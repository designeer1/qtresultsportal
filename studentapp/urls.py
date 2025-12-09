from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.view_result, name='view_result'),
]
