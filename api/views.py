from django.shortcuts import render
from rest_framework import viewsets
from .serializer import programmerSerializer,StuSerializer
from .models import programmer, Stu
# Create your views here.
class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = programmerSerializer
class StuViewSet(viewsets.ModelViewSet):
    queryset = Stu.objects.all()
    serializer_class =StuSerializer