from django.urls import path
from .views import DrivetListCreateAPIView, RetrieveDriverAPIView

urlpatterns = [
    path('create/', DrivetListCreateAPIView.as_view()),
    path('create/<int:pk>', RetrieveDriverAPIView.as_view()),
]