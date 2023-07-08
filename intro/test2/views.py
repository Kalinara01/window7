from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from . import serializers

@api_view(['GET'])
def get_sapros(request):
    vse_ludi = Person.objects.all()
    serializer = serializers.PersonSerializer(vse_ludi, many = True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def post_sapros(request):
    

