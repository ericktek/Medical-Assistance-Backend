from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from Main_app.serializers import *
from Main_app.models import *

class DiseaseView(ViewSet):
    '''
    Disease manegement view
    '''
    
    @extend_schema(
        tags=['Disease'],
        summary='Retrieve Disease',
        description='Retrieve a disease by id',

        responses={
            200: DiseaseSerializer,  404: 'Not found',
            }
    )
    def retrieve(self,request, pk=None):    
        qrset = Disease.objects.filter(pk=pk) 
        serializer = DiseaseSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Disease'],
        summary='delete Disease',
        description='delete a disease by id',
        responses={
            200: 'Delete',  404: 'Unable to delete',
            }
    )
    def destroy(self,request, pk=None):
        qrset = Disease.objects.filter(pk=pk)
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response("Unable to delete", status=status.HTTP_406_NOT_ACCEPTABLE)
    
    @extend_schema(
        tags=['Disease'],
        summary='List Disease',
        description='List all diseases',
        responses={
            200: DiseaseSerializer,
            }
    )
    def list(self,request):
        qrset = Disease.objects.all()
        serializer = DiseaseSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Disease'],
        summary='Create Disease',
        description='Create a new disease',
        request=DiseaseSerializer,
        responses={
            201: DiseaseSerializer, 400: 'Bad request',
            }
    )
    def create(self,request):
        serializer = DiseaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        tags=['Disease'],
        summary='Create Disease in bulk or single',
        description='Create Disease in single or multiple at once',
        request=[DiseaseSerializer],
        responses={
            200: DiseaseSerializer, 400: 'Bad request',
            })
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = DiseaseSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [Disease(**item) for item in request.data]
            Disease = Disease.objects.bulk_create(bulk_data)
            Disease_serializer = DiseaseSerializer(Disease, many=True)
            return Response(Disease_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=['Disease'],
        summary='update Disease',
        description='update a disease by id',
        request=DiseaseSerializer,
        responses={
            200: DiseaseSerializer,  404: 'Not found', 400: 'Bad request',
            }
    )
    def partial_update(self, request, pk=None):
        qrset = Disease.objects.filter(pk=pk).first() 
        serializer = DiseaseSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
