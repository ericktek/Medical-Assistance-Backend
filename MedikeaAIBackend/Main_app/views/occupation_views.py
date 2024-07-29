from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from Main_app.serializers import *
from Main_app.models import *

class OccupationView(ViewSet):
    '''
    Occupation manegement view
    '''
    
    @extend_schema(
        tags=['Occupation'],
        summary='Retrieve Occupation',
        description='Retrieve a occupation by id',
        responses={
            200: OccupationSerializer,  404: 'Not found',
            }
    )
    def retrieve(self,request, pk=None):
        qrset = Occupation.objects.filter(pk=pk) 
        serializer = OccupationSerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Occupation'],
        summary='delete Occupation',
        description='delete a occupation by id',
        responses={
            200: 'Delete',  404: 'Not found',
            }
    )
    def destroy(self,request, pk=None):
        qrset = Occupation.objects.filter(pk=pk)
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response("Unable to delete", status=status.HTTP_406_NOT_ACCEPTABLE)
    
    @extend_schema(
        tags=['Occupation'],
        summary='List Occupation',
        description='List all occupations',
        responses={
            200: OccupationSerializer,
            }
    )
    def list(self,request):
        qrset = Occupation.objects.all()
        serializer = OccupationSerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Occupation'],
        summary='Create Occupation',
        description='Create a new occupation',
        request=OccupationSerializer,
        responses={
            201: OccupationSerializer, 400: 'Bad request',
            }
    )
    def create(self,request):
        serializer = OccupationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        tags=['Occupation'],
        summary='update Occupation',
        description='update a occupation by id',
        request=OccupationSerializer,
        responses={
            200: OccupationSerializer,  404: 'Not found', 400: 'Bad request',
            }
    )
    def partial_update(self, request, pk=None):
        qrset = Occupation.objects.filter(pk=pk).first() 
        serializer = OccupationSerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        tags=['Occupation'],
        summary='Create Occupation in bulk or single',
        description='Create Occupation in single or multiple at once',
        request=[OccupationSerializer],
        responses={
            200: OccupationSerializer, 400: 'Bad request',
            }
        )
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = OccupationSerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [Occupation(**item) for item in request.data]
            Occupation = Occupation.objects.bulk_create(bulk_data)
            Occupation_serializer = OccupationSerializer(Occupation, many=True)
            return Response(Occupation_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
