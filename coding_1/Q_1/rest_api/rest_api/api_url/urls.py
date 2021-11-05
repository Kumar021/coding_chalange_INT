from django.urls import path
from candidates.views import (
     CandidateListView,
     CandidateDetailView

)

urlpatterns = [
    path('candidates/', CandidateListView.as_view(), name='candidate-list'),
    path('candidate/<pk>/', CandidateDetailView.as_view(), name='candidate-details')
]