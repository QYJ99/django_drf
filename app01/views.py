from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Student, Group
from .serializers import StudentSerializer, GroupSerializer

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()









