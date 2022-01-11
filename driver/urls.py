from django.urls import path
from .views import CreateDriverAPIView

urlpatterns = [
    path('create/', CreateDriverAPIView.as_view()),
]