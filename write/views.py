from django.shortcuts import render
from rest_framework import generics

from write.models import Write
from .models import Write
from .serializers import WriteSerializer
class WriteList(generics.ListCreateAPIView):
    queryset = Write.objects.all()
    serializer_class = WriteSerializer

class WriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Write.objects.all()
    serializer_class = WriteSerializer    