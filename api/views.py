from django.shortcuts import render
from rest_framework import generics
from api.models import ApiModel
from api.serializers import ApiSerializer
class API_objects(generics.ListCreateAPIView):
    queryset = ApiModel.objects.all()
    serializer_class = ApiSerializer
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApiModel.objects.all()
    serializer_class = ApiSerializer
