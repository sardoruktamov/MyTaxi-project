from django.urls import path
from .views import CreateOrderAPIView, AcceptOrderAPIView, OrderListAPIView, OrderStatusUpdateAPIView, FilterOrderAPIView

urlpatterns = [
    path('create/', CreateOrderAPIView.as_view()),
    path('accept/', AcceptOrderAPIView.as_view()),
    path('list/', OrderListAPIView.as_view()),
    path('<int:pk>/', OrderStatusUpdateAPIView.as_view()),
    path('filter/<int:pk>/', FilterOrderAPIView.as_view()),
]