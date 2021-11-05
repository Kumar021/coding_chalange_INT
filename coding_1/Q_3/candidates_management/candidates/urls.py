from django.urls import path
from .views import ( 
        candidates_create_view,
        CandidateView,
        CandidateUpdateView,
        CandidateDeleteView
    )

app_name = "candidates"

urlpatterns = [
    path('create/', candidates_create_view, name='create'),
    path('list/', CandidateView.as_view(), name='list'),
    path('update/<str:id>/', CandidateUpdateView.as_view(), name='update'),
    path('delete/<str:id>/', CandidateDeleteView.as_view(), name='delete'),
]