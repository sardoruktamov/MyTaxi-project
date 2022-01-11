from django.urls import path
from .views import CreateClientAPIView

urlpatterns = [
    path('create/', CreateClientAPIView.as_view()),
]