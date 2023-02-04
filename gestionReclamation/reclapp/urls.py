from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('entreprises/update/<str:pk>/' , views.update_entreprise , name="update-entreprise"),
    path('entreprises/delete/<str:pk>/', views.delete_entreprise, name="delete-entreprise"),
    path('entreprises/create/', views.create_entreprise , name="create-entreprise"),
    path('entreprises/<str:pk>/', views.entreprise, name="entreprise"),
    path('entreprises/', views.entreprises, name="entreprises"),
    path('clients/update/<str:pk>/' , views.update_client , name="update-client"),
    path('clients/delete/<str:pk>/', views.delete_client, name="delete-client"),
    path('clients/create/', views.create_client , name="create-client"),
    path('clients/<str:pk>/', views.client, name="client"),
    path('clients/', views.clients, name="clients"),
    path('reclamations/update/<str:pk>/' , views.update_reclamation , name="update-reclamation"),
    path('reclamations/delete/<str:pk>/', views.delete_reclamation, name="delete-reclamation"),
    path('reclamations/create/', views.create_reclamation , name="create-reclamation"),
    path('reclamations/<str:pk>/', views.reclamation, name="reclamation"),
    path('reclamations/', views.reclamations, name="reclamations")



]
