from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('add-result/', views.add_result, name='add_result'),
    path('edit-result/<int:id>/', views.edit_result, name='edit_result'),
    path('delete-result/<int:id>/', views.delete_result, name='delete_result'),
]

