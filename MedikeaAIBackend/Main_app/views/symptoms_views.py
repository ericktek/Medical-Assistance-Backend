from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from Main_app.serializers import *
from Main_app.models import *

class SymptomView(ViewSet):
    '''
    user symptom manegement
    '''
    
    @extend_schema(
        tags=['Symptom'],
        summary='Retrieve Symptom',
        description='Retrieve a symptom by id',
        responses={
            200: SymptomSerializer,  404: 'Not found',
            }
    )
    def retrieve(self,request, pk=None):
        qrset = Symptom.objects.filter(pk=pk) 
        serializer = SymptomSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    @extend_schema(
        tags=['Symptom'],
        summary='delete Symptom',
        description='delete a symptom by id',
        responses={
            200: 'Delete',  404: 'Not found',
            }
    )
    def destroy(self,request, pk=None):
        qrset = Symptom.objects.filter(pk=pk)
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response("Unable to delete", status=status.HTTP_404_NOT_FOUND)
    
    @extend_schema(
        tags=['Symptom'],
        summary='List Symptom',
        description='List all symptoms',
        responses={
            200: SymptomSerializer,
            }
    )   
    def list(self,request):
        qrset = Symptom.objects.all()
        serializer = SymptomSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Symptom'],
        summary='Create Symptom',
        description='Create a new symptom',
        request=SymptomSerializer,
        responses={
            201: SymptomSerializer, 400: 'Bad request',
            }
    )
    def create(self,request):
        serializer = SymptomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        tags=['Symptom'],
        summary='update Symptom',
        description='update a symptom by id',
        request=SymptomSerializer,
        responses={
            200: SymptomSerializer,  404: 'Not found', 400: 'Bad request',
            }
    )
    def partial_update(self, request, pk=None):
        qrset = Symptom.objects.filter(pk=pk).first() 
        serializer = SymptomSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        tags=['Symptom'],
        summary='Create Symptom in bulk or single',
        description='create multiple or single symptom at once',
        request=[SymptomSerializer],
        responses={
            200: SymptomSerializer, 400: 'Bad request',
            }
       )
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = SymptomSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [Symptom(**item) for item in request.data]
            Symptom = Symptom.objects.bulk_create(bulk_data)
            Symptom_serializer = SymptomSerializer(Symptom, many=True)
            return Response(Symptom_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

