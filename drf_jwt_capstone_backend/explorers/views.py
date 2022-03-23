from ast import Return
from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Explorer
from .serializers import ExplorerSerializer
from django.contrib.auth import get_user_model
User=get_user_model


@api_view(['POST'])
@permission_classes([AllowAny])
def create_explorer(request):
    serializer = ExplorerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # explorers = Explorer.objects.all()
    # serializer = ExplorerSerializer(explorers, many=True)
    # return Response(serializer.data)
@api_view(['GET','POST'])
@permission_classes ([IsAuthenticated])
def explorer_info(request):
    if request.method =='POST':
        serializer = ExplorerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='GET':
        explorers = Explorer.objects.filter(id=request.user.id)
        serializer = ExplorerSerializer(explorers, many=False)
        return Response(serializer.data)

    # serializer = ExplorerSerializer(data=request.data)
    
    # explorers = Explorer.objects.all()
    # serializer = ExplorerSerializer(explorers, many=True)
    # return Response(serializer.data)



# Create your views here.
