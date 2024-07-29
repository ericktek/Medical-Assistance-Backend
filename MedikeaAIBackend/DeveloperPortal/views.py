from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import generics
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from .models import *
from .serializers import *


class DeveloperViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class DeveloperDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

    @extend_schema(
        tags="Developer",
        summary="Retrieve Developer",
        description="Retrieve Developer by using id",
        responses={
            200:DeveloperSerializer, 400:{"message": "Permission denied"}
        }
        )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    @extend_schema(
        tags="Developer",
        summary="update Developer by using id",
        description="updating Developer by id",
        request=DeveloperSerializer,
        responses={
            200:DeveloperSerializer, 400:{"message": "Permission denied"}
        }
    )
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    @extend_schema(
        tags="Developer",
        summary="delete Developer by using id",
        description="deleting Developer by id",
        responses={
            200:DeveloperSerializer, 400:{"message": "Permission denied"}
        }
    )
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)

class ApiKeyViewSet(ViewSet):

    def create(self, request):
        serializer = UserApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def authenticate_api_key(self, request):
        username = request.data.get('username')
        api_key = request.data.get('api_key')

        data_dict = {"status":False, "message":"Permission denied", "data":None, "token":None}
        if username and api_key:
            users = UserApi.objects.filter(username=username, api_key=api_key)
            if users.exists():
                user = users.first()
                if not user.is_expired:
                    data_dict['satus']= True
                    data_dict['message'] = "Permission granted"
                    data_dict['data'] = user.first()
                    data_dict['token'] = user.token
                else:
                    data_dict['message'] = "Permission denied"
            else:
                data_dict['message'] = "Your api key has been expired please renew it again"
        return Response(data_dict, status=200)
