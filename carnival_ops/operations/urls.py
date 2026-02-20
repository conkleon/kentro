from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_team, name='add_team'),
    path('update/<int:team_id>/', views.update_status, name='update_status'),
    path('edit-details/<int:team_id>/', views.edit_team_details, name='edit_team_details'),
    path('delete/<int:team_id>/', views.delete_team, name='delete_team'),
]