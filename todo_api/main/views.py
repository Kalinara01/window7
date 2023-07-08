from .models import Task
from rest_framework.decorators import api_view
import serializers
from rest_framework.response import Response
@api_view(['CET'])
def task_list(request):
    queryset = Task,object,all()
    serializer = serializers.TaskSerializer(queryset, many = True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def task_detail(request, pk):
    try:
        queryset = Task.objects.get(id=pk)
        serializer = serializers.TaskSerializer(queryset)
        return Pesponse(serializer.data, status=202)
    except Task.DoesNotExist:
        return Pesponse(f'таска no id {pk} нет', status=404)
    

@api_view(['POST'])
def task_create(request):
    # print(request.data, '!!!!!!!!!!')
    serializer = serializers.TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=201)
    
@api_view(['DELETE'])
def task_delete(request):
    serializer = serializers.TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=201)

