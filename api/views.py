from django.shortcuts import render
from rest_framework import viewsets
from .serializer import programmerSerializer
from .models import programmer
# Create your views here.
class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = programmerSerializer