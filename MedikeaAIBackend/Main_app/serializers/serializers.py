from rest_framework.serializers import ModelSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import *
from  rest_framework import exceptions
from ..models import *

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def vlidate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')
        if username and password:
            user = authenticate(username = username, password = password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    msg = 'user account is blocked'
                    raise exceptions.ValidationError(msg)
            else:
                msg = 'Unable to login with given cridentials'
                raise exceptions.ValidationError(msg)

        else:
            msg = 'you must provide username or password'
            raise exceptions.ValidationError(msg)
        return data
    
class UserSerializer(serializers.Serializer):
    email = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    
    is_superuser = serializers.BooleanField()
    
    def validate(self, data):
        email = data.get('email', '')
        username = data.get('username', '')
        password = data.get('password', '')
        last_name = data.get('last_name', '')
        first_name = data.get('first_name', '')
        is_superuser = data.get('is_superuser', '')
        if email and password and username:
            if is_superuser:
                User.objects.create_superuser(email=email, username=username, password=password)
            else:
                
                User.objects.create_user(email=email, username=username, password=password)
            user = User.objects.get(username = username)
            user = User.objects.filter(username = email).first() 
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            data = user
            return data
        else:
            raise exceptions.ValidationError('all username, email, password and user role is required')

    class Meta:
        model = User
        fields = '__all__'

class SymptomSerializer(ModelSerializer):

    def validate(self, data):

        name = data.get('name', '')
        machine_learning_value = data.get('machine_learning_value', '')
        if name and machine_learning_value:
            existence_status = Symptom.objects.filter(name=name, machine_learning_value=machine_learning_value).exists()
            if existence_status:
                msg = 'Symptom already exists'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'Symptom name and machine_learning_value are required'
            raise exceptions.ValidationError(msg)
        
        return data
     
    def save(self, **kwargs):
        created_symptom = Symptom.objects.get_or_create(**self.validated_data)
        return created_symptom
    
    class Meta:
        model = Symptom
        fields = '__all__'

class SpecialitySerializer(ModelSerializer):

    def validate(self, data):

        name = data.get('name', '')
        if name:
            existence_status = Speciality.objects.filter(name=name).exists()
            if existence_status:
                msg = 'Speciality already exists'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'Speciality name is required'
            raise exceptions.ValidationError(msg)
        
        return data
     
    def save(self, **kwargs):
        created_Speciality = Speciality.objects.get_or_create(**self.validated_data)
        return created_Speciality
    
    class Meta:
        model = Speciality
        fields = '__all__'

class OccupationSerializer(ModelSerializer):

    def validate(self, data):
            
            name = data.get('name', '')
            machine_learning_value = data.get('machine_learning_value', '')
            if name and machine_learning_value:
                existence_status = Occupation.objects.filter(name=name, machine_learning_value=machine_learning_value).exists()
                if existence_status:
                    msg = 'Occupation already exists'
                    raise exceptions.ValidationError(msg)
            else:
                msg = 'Occupation name and machine_learning_value are required'
                raise exceptions.ValidationError(msg)
            
            return data 
    
    def save(self, **kwargs):
        created_occupation = Occupation.objects.get_or_create(**self.validated_data)
        return created_occupation
    
    class Meta:
        model = Occupation
        fields = '__all__'

class HospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class CommunitySerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'

class DoctorProfileSerializer(ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = '__all__'

class DrugstoreSerializer(ModelSerializer):
    class Meta:
        model = Drugstore
        fields = '__all__'
        
class TeatmentCategorySerializer(ModelSerializer):
    class Meta:
        model = TeatmentCategory
        fields = '__all__'

class TreatmentSerializer(ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'

class PharmacologicalTreatmentSerializer(ModelSerializer):
    class Meta:
        model = PharmacologicalTreatment
        fields = '__all__'
        
class DiseasePreventionSerializer(ModelSerializer):
    class Meta:
        model = DiseasePrevention
        fields = '__all__'

class DifferentialDiagnosisCategorySerializer(ModelSerializer):
    class Meta:
        model = DifferentialDiagnosisCategory
        fields = '__all__'

class DifferentialDiagnosisSerializer(ModelSerializer):
    class Meta:
        model = DifferentialDiagnosis
        fields = '__all__'

class InvestigationSerializer(ModelSerializer):
    class Meta:
        model = Investigation
        fields = '__all__'

class DiseaseSerializer(ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'  

class ModelTrainingResultSerializer(ModelSerializer):
    class Meta:
        model = ModelTrainingResult
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
    
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CaseSerializer(ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'

class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'
    
class PatientDetailSerializer(ModelSerializer):
    class Meta:
        model = PatientDetail
        fields = '__all__'