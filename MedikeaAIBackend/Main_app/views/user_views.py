from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from Main_app.serializers import *
from Main_app.models import *

class UserView(ViewSet):
    '''
    user manegement services
    '''
    
    @extend_schema(
        tags=['User'],
        summary='Retrieve User',
        description='Retrieve a user by id',
        responses={
            200: UserSerializer,  404: 'Not found',
            }
    )
    def retrieve(self,request, pk=None):
        qrset = User.objects.filter(pk=pk) 
        serializer = UserSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    @extend_schema(
        tags=['User'],
        summary='delete User',
        description='delete a user by id',
        responses={
            200: 'Delete',  404: 'Not found',
            }
    )
    def destroy(self,request, pk=None):
        qrset = User.objects.filter(pk=pk)
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response("Unable to delete", status=status.HTTP_406_NOT_ACCEPTABLE)
    
    @extend_schema(
        tags=['User'],
        summary='List User',
        description='List all users',
        responses={
            200: UserSerializer,
            }
    )   
    def list(self,request):
        qrset = User.objects.all()
        serializer = UserSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['User'],
        summary='Create User',
        description='Create a new user',
        request=UserSerializer,
        responses={
            201: UserSerializer, 400: 'Bad request',
            }
    )   
    def create(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        tags=['User'],
        summary='update User',
        description='update a user by id',
        request=UserSerializer,
        responses={
            200: UserSerializer,  404: 'Not found', 400: 'Bad request',
            }
    )
    def partial_update(self, request, pk=None):
        qrset = User.objects.filter(pk=pk).first() 
        serializer = UserSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        tags=['User'],
        summary='Create User in bulk or single',
        description='Create User in multiple or single at once',
        request=[UserSerializer],
        responses={
            201: UserSerializer, 400: 'Bad request',
            }
    )
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = UserSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [User(**item) for item in request.data]
            User = User.objects.bulk_create(bulk_data)
            User_serializer = UserSerializer(User, many=True)
            return Response(User_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

