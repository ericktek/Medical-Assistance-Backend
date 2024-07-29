from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from Main_app.serializers import *
from Main_app.models import *


class TreatmentView(ViewSet):
    '''
    Treatment manegement view
    '''
    
    @extend_schema(
        tags=['Treatment'],
        summary='Retrieve Treatment',
        description='Retrieve a treatment by id',
        responses={
            200: TreatmentSerializer,  404: 'Not found',
            }
    )
    def retrieve(self,request, pk=None):
        qrset = Treatment.objects.filter(pk=pk)
        if qrset.exists():
            serializer = TreatmentSerializer(qrset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)
    
    @extend_schema(
        tags=['Treatment'],
        summary='delete Treatment',
        description='delete a treatment by id',
        responses={
            200: 'Delete',  404: 'Unable to delete',
            }
    )
    def destroy(self,request, pk=None):
        qrset = Treatment.objects.filter(pk=pk)
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response("Unable to delete", status=status.HTTP_404_NOT_FOUND)
    
    @extend_schema(
        tags=['Treatment'],
        summary='List Treatment',
        description='List all treatments',
        responses={
            200: TreatmentSerializer,
            }
    )
    def list(self,request):
        qrset = Treatment.objects.all()
        serializer = TreatmentSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Treatment'],
        summary='Create Treatment',
        description='Create a new treatment',
        request=TreatmentSerializer,
        responses={
            201: TreatmentSerializer, 400: 'Bad request',
            }
    )
    def create(self,request):
        serializer = TreatmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        tags=['Treatment'],
        summary='update Treatment',
        description='update a treatment by id',
        request=TreatmentSerializer,
        responses={
            200: TreatmentSerializer,  404: 'Not found', 400: 'Bad request',
            }
    )   
    def partial_update(self, request, pk=None):
        qrset = Treatment.objects.filter(pk=pk).first() 
        serializer = TreatmentSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        tags=['Treatment'],
        summary='Create Treatment in bulk or single',
        description='Create Treatment in single or multiple at once',
        request=[TreatmentSerializer],
        responses={
            200: TreatmentSerializer, 400: 'Bad request',
            })
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = TreatmentSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [Treatment(**item) for item in request.data]
            Treatment = Treatment.objects.bulk_create(bulk_data)
            Treatment_serializer = TreatmentSerializer(Treatment, many=True)
            return Response(Treatment_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
