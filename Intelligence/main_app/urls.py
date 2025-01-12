from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('request-dataset/', views.requestDataset, name='request-dataset'),
    path('data-entry/', views.dataEntry, name='data-entry'),
    path('model-data/', views.modelData, name='model-data'),
    path('confirm/', views.confirmation, name='confirm'),
    path('history/', views.history, name='history'),
    path('api/records/', views.RecordListAPIView.as_view(), name="record-list")
]