from django.urls import path
from .views import CreateOrderAPIView, AcceptOrderAPIView, OrderListAPIView

urlpatterns = [
    path('create/', CreateOrderAPIView.as_view()),
    path('accept/', AcceptOrderAPIView.as_view()),
    path('list/', OrderListAPIView.as_view()),
]