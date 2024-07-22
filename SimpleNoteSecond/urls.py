from django.urls import path
from .views import index_views, Notes_view, Add_view, Edit_view, Delete_view

urlpatterns = [
    path('', index_views, name='index'),
    path('Notes/<str:title>/', Notes_view, name='notes'),
    path('Add/', Add_view, name='add'),
    path('Edit/<str:title>/', Edit_view, name='edit'),
    path('Delete/<str:title>/', Delete_view, name='delete'),
]
