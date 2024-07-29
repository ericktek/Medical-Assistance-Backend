from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from Main_app.serializers import *
from Main_app.models import *

class TeatmentCategoryView(ViewSet):
    '''
    Teatment Category manegement view
    '''
    
    @extend_schema(
        tags=['Teatment Category'],
        summary='Retrieve Teatment Category',
        description='Retrieve a teatment category by id',
        responses={
            200: TeatmentCategorySerializer,  404: 'Not found',
            }
    )
    def retrieve(self,request, pk=None):
        qrset = TeatmentCategory.objects.filter(pk=pk) 
        serializer = TeatmentCategorySerializer(qrset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Teatment Category'],
        summary='delete Teatment Category',
        description='delete a teatment category by id',
        responses={
            200: 'Delete',  404: 'Not found',
            }
    )
    def destroy(self,request, pk=None):
        qrset = TeatmentCategory.objects.filter(pk=pk)
        if qrset.exists():
            qrset.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        return Response("Unable to delete", status=status.HTTP_406_NOT_ACCEPTABLE)
    
    @extend_schema(
        tags=['Teatment Category'],
        summary='List Teatment Category',
        description='List all teatment categories',
        responses={
            200: TeatmentCategorySerializer,
            }
    )
    def list(self,request):
        qrset = TeatmentCategory.objects.all()
        serializer = TeatmentCategorySerializer(qrset, many=True, )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Teatment Category'],
        summary='Create Teatment Category',
        description='Create a new teatment category',
        request=TeatmentCategorySerializer,
        responses={
            201: TeatmentCategorySerializer, 400: 'Bad request',
            }
    )
    def create(self,request):
        serializer = TeatmentCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        tags=['Teatment Category'],
        summary='update Teatment Category',
        description='update a teatment category by id',
        request=TeatmentCategorySerializer,
        responses={
            200: TeatmentCategorySerializer,  404: 'Not found', 400: 'Bad request',
            }
    )   
    def partial_update(self, request, pk=None):
        qrset = TeatmentCategory.objects.filter(pk=pk).first() 
        serializer = TeatmentCategorySerializer(instance=qrset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        tags=['Teatment Category'],
        summary='Create Teatment Category in bulk or single',
        description='Create Teatment Category in single or multiple at once',
        request=[TeatmentCategorySerializer],
        responses={
            200: TeatmentCategorySerializer, 400: 'Bad request',
            })
    def create_in_builk_or_single(self,request):
        check_data = request.data[0]
        serializer = TeatmentCategorySerializer(data=check_data)
        if serializer.is_valid():
            bulk_data = [TeatmentCategory(**item) for item in request.data]
            TeatmentCategory = TeatmentCategory.objects.bulk_create(bulk_data)
            TeatmentCategory_serializer = TeatmentCategorySerializer(TeatmentCategory, many=True)
            return Response(TeatmentCategory_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
