from django.urls import path
from .views import (
        candidates_list_view, 
        candidates_delete_view, 
        candidates_create_view,
        candidates_update_view
    )

app_name = "candidates"

urlpatterns = [
    path('list/', candidates_list_view, name='list'),
    path('delete/<int:id>/', candidates_delete_view, name='delete'),
    path('create/', candidates_create_view, name='create'),
    path('update/<int:id>/', candidates_update_view, name='update'),
]