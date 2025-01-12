from django.urls import path
from .views import ReceiveDataAPIView, CustomObtainAuthToken

urlpatterns = [
    path('receive-data/', ReceiveDataAPIView.as_view(), name='receive_data'),
    path('receive-data/<int:pk>/', ReceiveDataAPIView.as_view(), name='detail'),
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
]