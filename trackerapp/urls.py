from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="list"),
    path('edit_item/<str:pk>/', views.editItem, name="edit_item"),
    path('delete/<str:pk>/', views.deleteItem, name="delete"),
]
