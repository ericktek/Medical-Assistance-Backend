from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import *
from  rest_framework import exceptions
from ..models import *

class SymptomDepthSerializer(ModelSerializer):

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
        depth = 4

class SpecialityDepthSerializer(ModelSerializer):

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
        depth = 4

class OccupationDepthSerializer(ModelSerializer):

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
        depth = 4

class HospitalDepthSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
        depth = 4

class CommunityDepthSerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'
        depth = 4

class DoctorProfileDepthSerializer(ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = '__all__'
        depth = 4

class DrugstoreDepthSerializer(ModelSerializer):
    class Meta:
        model = Drugstore
        fields = '__all__'
        depth = 4

class TeatmentCategoryDepthSerializer(ModelSerializer):
    class Meta:
        model = TeatmentCategory
        fields = '__all__'
        depth = 4

class TreatmentDepthSerializer(ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'
        depth = 4

class PharmacologicalTreatmentDepthSerializer(ModelSerializer):
    class Meta:
        model = PharmacologicalTreatment
        fields = '__all__'
        depth = 4

class DiseasePreventionDepthSerializer(ModelSerializer):
    class Meta:
        model = DiseasePrevention
        fields = '__all__'
        depth = 4

class DifferentialDiagnosisCategoryDepthSerializer(ModelSerializer):
    class Meta:
        model = DifferentialDiagnosisCategory
        fields = '__all__'
        depth = 4

class DifferentialDiagnosisDepthSerializer(ModelSerializer):
    class Meta:
        model = DifferentialDiagnosis
        fields = '__all__'
        depth = 4

class InvestigationDepthSerializer(ModelSerializer):
    class Meta:
        model = Investigation
        fields = '__all__'
        depth = 4

class DiseaseDepthSerializer(ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'  

class ModelTrainingResultDepthSerializer(ModelSerializer):
    class Meta:
        model = ModelTrainingResult
        fields = '__all__'
        depth = 4

class MessageDepthSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        depth = 4

class PostDepthSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 4

class CommentDepthSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 4

class LikeDepthSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        depth = 4

class CaseDepthSerializer(ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'
        depth = 4

class ResourceDepthSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'
        depth = 4

class PatientDetailDepthSerializer(ModelSerializer):
    class Meta:
        model = PatientDetail
        fields = '__all__'
        depth = 4