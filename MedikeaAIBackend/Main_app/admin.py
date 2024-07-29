from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.db import models

from .models import *

class OccupationAdmin(admin.ModelAdmin):
    list_display = ['name', 'machine_learning_value', 'created_at', 'updated_at']
    search_fields = ['name', 'machine_learning_value']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']  # Make created_at and updated_at readonly
    fieldsets = (
        (None, {
            'fields': ('name', 'machine_learning_value')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapse the Timestamps section initially
        }),
    )

admin.site.register(Occupation, OccupationAdmin)


class CustomUserAdmin(BaseUserAdmin):
    # Define fieldsets to organize fields in add/change forms
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'date_birth', 'occupation', 'profile', 'gender', 'latitude')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # Define list_display to customize columns in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', "phone_number", 'date_birth', 'occupation', 'is_staff')
    # Define search_fields to enable searching by specific fields
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # Define ordering to specify default ordering
    ordering = ('-date_joined',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

# Register the User model with the custom admin class
admin.site.register(User, CustomUserAdmin)


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'level', 'created_by', 'created_at', 'updated_at']
    # Define search fields to enable searching by specific fields
    search_fields = ['name', 'description', 'level']
    list_filter = ['level', 'created_at', 'updated_at']
    readonly_fields = ['created_by']

admin.site.register(Speciality, SpecialityAdmin)

class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'description', 'phone_number', 'level', 'created_by', 'created_at', 'updated_at']
    # Define search fields to enable searching by specific fields
    search_fields = ['name', 'location', 'phone_number', 'level']
    list_filter = ['level', 'created_at', 'updated_at']
    readonly_fields = ['created_by']

admin.site.register(Hospital, HospitalAdmin)

class CommunityAdmin(admin.ModelAdmin):
    # Define fields to display in the list view
    list_display = ['name', 'description', 'created_by', 'created_at', 'updated_at']
    # Define search fields to enable searching by specific fields
    search_fields = ['name', 'description']
    # Make the created_by field readonly
    readonly_fields = ['created_by']
    

admin.site.register(Community, CommunityAdmin)

# class DoctorProfileAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'speciality', 'address', 'verification_status']
#     search_fields = ['user__username', 'user__email', 'speciality__name']
#     list_filter = ['speciality', 'verification_status']
#     readonly_fields = ['created_at', 'updated_at']  # Make created_at and updated_at readonly
#     fieldsets = (
#         (None, {
#             'fields': ('user', 'address', 'verification_status')
#         }),
#         ('Specialization', {
#             'fields': ('speciality',),
#         }),
#         ('Associations', {
#             'fields': ('hospital', 'community'),
#         }),
#         ('Timestamps', {
#             'fields': ('created_at', 'updated_at'),
#             'classes': ('collapse',)  # Collapse the Timestamps section initially
#         }),
#     )

# admin.site.register(DoctorProfile, DoctorProfileAdmin)


class DrugstoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dosage_form', 'strength', 'sub_categories']
    search_fields = ['name', 'dosage_form']
    list_filter = ['level']
    readonly_fields = ['created_at', 'updated_at']  # Make created_at and updated_at readonly
    fieldsets = (
        (None, {
            'fields': ('name', 'dosage_form', 'level')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapse the Timestamps section initially
        }),
    )

admin.site.register(Drugstore, DrugstoreAdmin)

class TeatmentCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']  # Make created_at and updated_at readonly
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ("user Information", {
            'fields': ('created_by', 'updated_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapse the Timestamps section initially
        }),
    )

admin.site.register(TeatmentCategory, TeatmentCategoryAdmin)

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_by', 'updated_by']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']  # Make created_at and updated_at readonly
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ("user Information", {
            'fields': ('created_by', 'updated_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapse the Timestamps section initially
        }),
    )

admin.site.register(Treatment, TreatmentAdmin)

class PharmacologicalTreatmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'usage_form', 'weight', 'dose_unit', 'dose_time', 'dose_time_unit', 'total_duration', 'total_duration_unit', 'condition', 'created_by', 'updated_by']
    search_fields = ['usage_form', 'condition']
    readonly_fields = ['created_at', 'updated_at']  # Make created_at and updated_at readonly
    fieldsets = (
        (None, {
            'fields': ('usage_form', 'weight', 'dose_unit', 'dose_time', 'dose_time_unit', 'total_duration', 'total_duration_unit', 'condition')
        }),
        ('Additional Information', {
            'fields': ('allowed_group', 'warnings', 'alternative_drug', 'drugs')
        }),
        ('User Information', {
            'fields': ('created_by', 'updated_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapse the Timestamps section initially
        }),
    )
    # Define fieldsets as tabs
    fieldsets = [
        ('Details', {
            'fields': ('usage_form', 'weight', 'dose_unit', 'dose_time', 'dose_time_unit', 'total_duration', 'total_duration_unit', 'condition'),
        }),
        ('Additional Information', {
            'fields': ('allowed_group', 'warnings', 'alternative_drug', 'drugs'),
        }),
        ('User Information', {
            'fields': ('created_by', 'updated_by'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapse the Timestamps section initially
        }),
    ]

admin.site.register(PharmacologicalTreatment, PharmacologicalTreatmentAdmin)


class SymptomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'machine_learning_value', 'created_by', 'updated_by']
    search_fields = ['name', 'machine_learning_value']
    readonly_fields = ['created_at', 'updated_at']  # Make created_at and updated_at readonly
    fieldsets = (
        (None, {
            'fields': ('name', 'machine_learning_value')
        }),
        ('User Information', {
            'fields': ('created_by', 'updated_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapse the Timestamps section initially
        }),
    )

admin.site.register(Symptom, SymptomAdmin)

class DiseasePreventionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_by', 'updated_by']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']  # Make created_at and updated_at readonly
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('User Information', {
            'fields': ('created_by', 'updated_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapse the Timestamps section initially
        }),
    )

admin.site.register(DiseasePrevention, DiseasePreventionAdmin)

class DifferentialDiagnosisAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'created_by', 'updated_by']
    search_fields = ['name', 'description']
    list_filter = ['category']
    readonly_fields = ['created_at', 'updated_at']  # Make created_at and updated_at readonly
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'category')
        }),
        ('User Information', {
            'fields': ('created_by', 'updated_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapse the Timestamps section initially
        }),
    )

admin.site.register(DifferentialDiagnosis, DifferentialDiagnosisAdmin)

class InvestigationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']  # Make created_at and updated_at readonly

admin.site.register(Investigation, InvestigationsAdmin)

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_by', 'updated_by']
    search_fields = ['name', 'description']
    list_filter = ['name']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ("other Meta Data", {
            'fields': ('occupation', 'referal_conditions', "symptoms", "differential_diagnosis", "causes", "investigations", "prevention", "pharmacological_treatment", "treatment")
        }),
        ('User Information', {
            'fields': ('created_by', 'updated_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Disease, DiseaseAdmin)

class ModelTrainingResultsAdmin(admin.ModelAdmin):
    list_display = ['id', 'model_name', 'accuracy', 'precision', 'recall', 'created_at', 'updated_at']
    search_fields = ['model_name']
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(ModelTrainingResult, ModelTrainingResultsAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'receiver', 'content', 'status', 'is_read', 'created_at', 'updated_at']
    search_fields = ['content']
    list_filter = ['status', 'is_read']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        (None, {
            'fields': ('sender', 'receiver', 'content')
        }),
        ('Message Status', {
            'fields': ('status', 'is_read')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Message, MessageAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'user', 'community', 'created_by', 'updated_by', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    list_filter = ['user', 'community']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ('Post Details', {
            'fields': ('user', 'community')
        }),
        ('Admin Information', {
            'fields': ('created_by', 'updated_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user', 'content', 'created_by', 'updated_by', 'created_at', 'updated_at']
    search_fields = ['content']
    list_filter = ['post', 'user']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        (None, {
            'fields': ('post', 'user')
        }),
        ('Comment Details', {
            'fields': ('content',)
        }),
        ('Admin Information', {
            'fields': ('created_by', 'updated_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Comment, CommentAdmin)

class CasesAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'location', 'gender', 'target_group', 'created_by', 'updated_by', 'created_at', 'updated_at']
    search_fields = ['age', 'location', 'gender', 'target_group']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Patient Information', {
            'fields': ('age', 'location', 'gender', 'target_group')
        }),
        ('Vital Signs', {
            'fields': ('body_temperature', 'spo2', 'normal_pulse', 'systolic_blood_pressure', 'diastolic_blood_pressure', 'respiratory_rate', 'bmi')
        }),
        ('Medical History', {
            'fields': ('patient_hpi', 'physical_examination', 'diisease_id')
        }),
        ('Treatment and Outcome', {
            'fields': ('treatment', 'outcome')
        }),
        ('Admin Information', {
            'fields': ('created_by', 'updated_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    # Customize tabs
    fieldsets = [
        ('Patient Information', {'fields': ('age', 'location', 'gender', 'target_group')}),
        ('Vital Signs', {'fields': ('body_temperature', 'spo2', 'normal_pulse', 'systolic_blood_pressure', 'diastolic_blood_pressure', 'respiratory_rate', 'bmi')}),
        ('Medical History', {'fields': ('patient_hpi', 'physical_examination', 'diisease_id')}),
        ('Treatment and Outcome', {'fields': ('treatment', 'outcome')}),
        ('Admin Information', {'fields': ('created_by', 'updated_by')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ['collapse']}),
    ]

admin.site.register(Case, CasesAdmin)

class ResourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'resource_type', 'created_by', 'updated_by', 'created_at', 'updated_at']
    search_fields = ['title', 'description', 'resource_type']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Resource Information', {
            'fields': ('title', 'description', 'resource_type', 'file_path', 'link')
        }),
        ('Admin Information', {
            'fields': ('created_by', 'updated_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    # Customize tabs
    fieldsets = [
        ('Resource Information', {'fields': ('title', 'description', 'resource_type', 'file_path', 'link')}),
        ('Admin Information', {'fields': ('created_by', 'updated_by')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ['collapse']}),
    ]

admin.site.register(Resource, ResourceAdmin)

class PatientDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'age', 'location', 'gender', 'target_group', 'created_at', 'updated_at']
    search_fields = ['location', 'gender', 'target_group']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Symptoms', {
            'fields': ('main_symptoms', 'associed_symptoms', 'patient_hpi', 'physical_examination')
        }),
        ('Patient Information', {
            'fields': ('age', 'gender', 'occupation', 'location', 'target_group', 'body_temperature', 'spo2', 'normal_pulse', 'systolic_blood_pressure', 'diastolic_blood_pressure', 'bmi', 'respiratory_rate')
        }),
        ('Medical Information', {
            'fields': ('diseases', 'investigations', 'prescriptions', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    # Customize tabs
    fieldsets = [
        ('Symptoms', {'fields': ('main_symptoms', 'associed_symptoms', 'patient_hpi', 'physical_examination')}),
        ('Patient Information', {'fields': ('age', 'gender', 'occupation', 'location', 'target_group', 'body_temperature', 'spo2', 'normal_pulse', 'systolic_blood_pressure', 'diastolic_blood_pressure', 'bmi', 'respiratory_rate')}),
        ('Medical Information', {'fields': ('diseases', 'investigations', 'prescriptions', 'status')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ['collapse']}),
    ]

admin.site.register(PatientDetail, PatientDetailAdmin)
