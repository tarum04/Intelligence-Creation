from django.shortcuts import render
from rest_framework import generics
from .models import Record
from .serializers import RecordSerializer

# Create your views here.
def index(request):
    return render(request, 'main/dashboard.html')

def dataEntry(request):
    return render(request, 'main/dataEntry.html')

def modelData(request):
    return render(request, 'main/modelData.html')

def requestDataset(request):
    return render(request, 'main/request_dataset.html')

def confirmation(request):
    return render(request, 'main/confirm.html')

def history(request):
    return render(request, 'main/history.html')

# OUR API
class RecordListAPIView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer