from django.urls import path
from .views import CreateOrderAPIView, AcceptOrderAPIView

urlpatterns = [
    path('create/', CreateOrderAPIView.as_view()),
    path('accept/', AcceptOrderAPIView.as_view()),
]