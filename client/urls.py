from django.urls import path
from .views import ClientListCreateAPIView, RetrieveClientAPIView

urlpatterns = [
    path('create/', ClientListCreateAPIView.as_view()),
    path('create/<int:pk>', RetrieveClientAPIView.as_view()),
]