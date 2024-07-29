from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4
from django.conf import Settings
from django.utils import timezone

# from .utils.utils import encrypt_message
from .utils.costants import *


class Occupation(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True,
                           default=uuid4)
    name = models.CharField(max_length=255)            
    machine_learning_value = models.CharField(max_length=255, null=True, blank=True)          
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = 'Occupation'
        verbose_name_plural = 'Occupation'
        db_table = 'Occupation'

class User(AbstractUser):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    phone_number = models.CharField(max_length=20, unique=True)
    date_birth = models.DateField(null=True, blank=True)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ImageField(blank=True, null=True, default='profile.png')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'

class ServiceLevel(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)   

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Service level'
        verbose_name_plural = 'Service levels'
        db_table = 'Service_level'

class ProfessionalExpertise(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    levels = models.ManyToManyField(ServiceLevel)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Professional expertise'
        verbose_name_plural = 'Professional expertise'
        db_table = 'professional_expertise'

class ServiceProvision(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    levels = models.ManyToManyField(ServiceLevel)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Service provision'
        verbose_name_plural = 'Service provisions'
        db_table = 'service_provision'

class Speciality(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    icon = models.ImageField(upload_to='media/speciality', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='speciality_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='speciality_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)   
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'
        db_table = 'specialties'

class Hospital(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    icon = models.ImageField(upload_to='media/hospital', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hospital_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hospital_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)   
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitals'
        db_table = 'hospitals'

class Community(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)   
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Community'
        verbose_name_plural = 'Communities'
        db_table = 'communities'

class DoctorProfile(User):
    address = models.CharField(max_length=50)
    verification_status = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='media/profile_picture', null=True, blank=True)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    hospital = models.ManyToManyField(Hospital)
    community = models.ManyToManyField(Community)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_profile_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_profile_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'
        db_table = 'doctors'  

class DrugCategory(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    name = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Drug category'
        verbose_name_plural = 'Drug categories'
        db_table = 'drug_categories'

class Drugstore(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)            
    dosage_form= models.TextField(blank=True, null=True)
    strength = models.TextField(blank=True, null=True)
    level = models.ForeignKey(ServiceLevel, on_delete=models.CASCADE)
    sub_categories = models.TextField(blank=True, null=True)
    drug_category = models.ForeignKey(DrugCategory, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='drugstore_created_by', blank=True, null=True) 
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='drugstore_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Drug store'
        verbose_name_plural = 'Drug stores'
        db_table = 'drug stores'

class TeatmentCategory(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True,
                           default=uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    machine_learning_value = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='treatment_category_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='treatment_category_updated_by', blank=True, null=True)            
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
                
    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = 'Teatment categories'
        verbose_name_plural = 'Teatment categories'
        db_table = 'treatment_categories'

class Treatment(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True,
                           default=uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    treatment_category = models.ForeignKey(TeatmentCategory, on_delete=models.CASCADE)
    recommendations = models.JSONField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='treatment_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='treatment_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = 'treatment'
        verbose_name_plural = 'treatments'
        db_table = 'treatments'

class PharmacologicalTreatment(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    usage_form = models.CharField(max_length=255, default="oral") #eg. oral, injection
    weight = models.CharField(max_length=50)
    dose_unit = models.CharField(max_length=255)   #eg. 2 tablets
    dose_time = models.IntegerField(default=8) # eg 8, 12, 24
    dose_time_unit = models.CharField(max_length=255) # eg. hours, minutes, days
    total_duration = models.IntegerField(default=1) # eg 5
    total_duration_unit = models.CharField(max_length=255) # eg. days, weeks, months   
    condition = models.CharField(max_length=255) #eg. Control hypertension (for SBP>90mmHg)      
    allowed_group = models.JSONField(blank=True, null=True) #eg. Adults, children
    warnings = models.TextField(blank=True, null=True) #eg. if patient still seizing
    alternative_drug = models.JSONField(blank=True, null=True) # Passing ids of pharmacological treatment
    drugs = models.ForeignKey(Drugstore, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pharmacological_treatment_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pharmacological_treatment_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Pharmacological treatment'
        verbose_name_plural = 'Pharmacological treatments'
        db_table = 'pharmacological_treatments' 

class Symptom(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True,
                           default=uuid4)
    name = models.CharField(max_length=255)            
    machine_learning_value = models.CharField(max_length=255, null=True, blank=True)         
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='symptom_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='symptom_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = 'Symptom'
        verbose_name_plural = 'Symptoms'
        db_table = 'symptoms'

class DiseasePrevention(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disease_prevention_created_by', null=True, blank= True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disease_prevention_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Disease Prevention'
        verbose_name_plural = 'Disease Prevention'
        db_table = 'disease_prevents'

class DifferentialDiagnosisCategory(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)            
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='differential_diagnosis_category_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='differential_diagnosis_category_updated_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Differential Diagnosis Category'
        verbose_name_plural = 'Differential Diagnosis Category'
        db_table = 'differential_diagnosis_categories'

class DifferentialDiagnosis(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)            
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(DifferentialDiagnosisCategory, on_delete=models.PROTECT, null=True, blank = True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='differential_diagnosis_created_by', null=True, blank= True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="differential_diagnosis_updated_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Differential Diagnosis'
        verbose_name_plural = 'Differential Diagnosis'
        db_table = 'differential_diagnosis'

class Investigation(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Investigation'
        verbose_name_plural = 'Investigations'
        db_table = 'investigations'    
        
class Disease(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)            
    machine_learning_value = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.JSONField(blank=True, null=True)
    referal_conditions = models.JSONField(blank=True, null=True)
    symptoms = models.ManyToManyField(Symptom)
    differential_diagnosis = models.ManyToManyField(DifferentialDiagnosis)
    causes = models.JSONField(blank=True, null=True)
    notes = models.JSONField(blank=True, null=True)
    indications = models.JSONField(blank=True, null=True)
    contraindications = models.JSONField(blank=True, null=True)
    investigations = models.ManyToManyField(Investigation)
    prevention = models.ManyToManyField(DiseasePrevention)
    pharmacological_treatment = models.ManyToManyField(PharmacologicalTreatment)
    treatment = models.ManyToManyField(Treatment)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disease_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='disease_updated_by', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Disease'
        verbose_name_plural = 'Diseases'
        db_table = 'diseases'
    
class ModelTrainingResult(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    model_name = models.CharField(max_length=255)
    model_file = models.FileField(upload_to='media/model', null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    recall = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Model Training Result'
        verbose_name_plural = 'Model Training Results'
        db_table = 'Model Training Results'

class Message(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    sender = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'sender',  blank=True, null=True)            
    receiver = models.ForeignKey(User, on_delete= models.CASCADE, related_name = 'receiver',  blank=True, null=True)            
    content = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='active')
    is_read = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_updated_by', blank=True, null=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_deleted_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        db_table = 'messages'

class Post(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    tags = models.JSONField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user', blank=True, null=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='post_community', blank=True, null=True)
    image = models.ImageField(upload_to='media/post', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'posts'

class Comment(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    content = models.TextField(blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'Comment'

class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user', blank=True, null=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        db_table = 'Like'
        
class Case(models.Model):
    patient_hpi = models.JSONField()
    physical_examination = models.JSONField()
    age = models.IntegerField()
    body_temperature = models.FloatField()
    spo2 = models.FloatField()
    occupation = models.CharField(max_length=50)
    normal_pulse = models.IntegerField()
    systolic_blood_pressure = models.IntegerField()
    diastolic_blood_pressure = models.IntegerField()
    bmi = models.FloatField()
    location = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    target_group = models.CharField(max_length=50)
    respiratory_rate = models.IntegerField()
    diisease_id = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='cases_disease', blank=True, null=True)
    treatment = models.JSONField(blank=True, null=True)
    outcome = models.JSONField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cases_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cases_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'
        db_table = 'Cases'

class Resource(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    file_path = models.FileField(upload_to='media/resource', null=True, blank=True)
    link = models.CharField(max_length=50, blank=True, null=True)
    resource_type = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resource_created_by', blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resource_updated_by', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'resource'
        verbose_name_plural = 'resources'
        db_table = 'resources'

class PatientDetail(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    main_symptoms = models.JSONField()
    associated_symptoms = models.JSONField()
    patient_hpi = models.JSONField()
    physical_examination = models.JSONField()
    age = models.BigIntegerField()
    body_temperature = models.FloatField()
    spo2 = models.FloatField()
    occupation = models.CharField(max_length=50)
    normal_pulse = models.BigIntegerField(default=80)
    systolic_blood_pressure = models.BigIntegerField(default=120)
    diastolic_blood_pressure = models.BigIntegerField(default=80)
    bmi = models.FloatField()
    location = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    target_group = models.CharField(max_length=50)
    respiratory_rate = models.BigIntegerField(default=10)
    diseases = models.JSONField(null=True, blank=True)
    investigations = models.JSONField(null=True, blank=True)
    prescriptions = models.JSONField(null=True, blank=True)
    status = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # key = Settings.Encryption_key
        # self.patient_id = encrypt_message(self.id, key)
        # self.main_symptoms =[encrypt_message(symptom, key) for symptom in self.main_symptoms]
        # self.associed_symptoms = [encrypt_message(symptom, key) for symptom in self.associed_symptoms]
        # self.patient_hpi = [encrypt_message(symptom, key) for symptom in self.patient_hpi]
        # self.physical_examination = [encrypt_message(symptom, key) for symptom in self.physical_examination]
        # self.occupation = encrypt_message(self.occupation, key)
        # self.location = encrypt_message(self.location, key)
        # self.gender = encrypt_message(self.gender, key)
        # self.target_group = encrypt_message(self.target_group, key)
        # self.diseases = [encrypt_message(disease, key) for disease in self.diseases]
        # self.investigations = [encrypt_message(investigation, key) for investigation in self.investigations]
        # self.prescriptions = [encrypt_message(prescription, key) for prescription in self.prescriptions]
        # self.status = [encrypt_message(status, key) for status in self.status]
        super(PatientDetail, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.patient_id
    class Meta:
        verbose_name = 'PatientDiteail'
        verbose_name_plural = 'PatientDiteail'
        db_table = 'PatientDiteail'
