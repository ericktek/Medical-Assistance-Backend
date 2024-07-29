from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from Main_app.serializers import *
from Main_app.models import *

class SpecialityView(ViewSet):
    '''
    specialist manegement services
    '''
    
    @extend_schema(
        tags=['Speciality'],
        summary='Create Speciality',
        description='Create a new speciality',
        request=SpecialitySerializer,
        responses={
            201: SpecialitySerializer, 400: 'Bad request',
            }
    )
    def create(self, request):
        serializer = SpecialitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=['Speciality'],
        summary='Retrieve Speciality',
        description='Retrieve a speciality by id',
        responses={
            200: SpecialitySerializer,  404: 'Not found',
            }
    )
    def retrieve(self, request, pk=None):
        details =  Speciality.objects.filter(pk=pk)
        if details.exists():
            serializer = SpecialitySerializer(details)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Not found", status=status.HTTP_404_NOT_FOUND)


    @extend_schema(
        tags=['Speciality'],
        summary='delete Speciality',
        description='delete a speciality by id',
        responses={
            200: 'Delete',  404: 'Not found',
            }
    )
    def destroy(self, request, pk=None):
        Speciality_ =  Speciality.objects.filter(pk=pk)
        Speciality_.delete()
        return Response("Delete", status=status.HTTP_200_OK)
    
    @extend_schema(
        tags=['Speciality'],
        summary='update Speciality',
        description='update a speciality by id',
        request=SpecialitySerializer,
        responses={
            200: SpecialitySerializer,  404: 'Not found', 400: 'Bad request',
            }
    )   
    def partial_update(self, request, pk=None):
        queryset = Speciality.objects.filter(pk=pk)
        serializer = SpecialitySerializer(
            instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        tags=['Speciality'],
        summary='List Speciality',
        description='List all specialities',
        responses={
            200: SpecialitySerializer,
            }
    )
    def list(self, request):
        query = Speciality.objects.all()
        serializer = SpecialitySerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
