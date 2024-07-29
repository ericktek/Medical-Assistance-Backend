from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('initilize', views.initilize, name='initilize'),

    # ===================== Speciality ===========================================================
    
    path('speciality', SpecialityView.as_view({
        'post':'create',
        'get':'list'
    })),
    path('speciality/<str:pk>', SpecialityView.as_view({
        'get':'retrieve',
        'patch':'partial_update',
        'delete':'destroy'
    })),

    # ===================== SYMPTOM ===========================================================

  path('symptom',   SymptomView.as_view({
        'post':'create',
        'get':'list'
        })),
  path('symptom/<str:pk>',   SymptomView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
        })),

      # ===================== OCCUPATION ===========================================================

  path('occupation',   OccupationView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('occupation/<str:pk>',   OccupationView.as_view({
        'patch':'partial_update',
        'delete':'destroy'
        })), 

      # ===================== TEATMENT CATEGORY ===========================================================

  path('teatmentCategory',   TeatmentCategoryView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('treatmentCategory/<str:pk>',   TeatmentCategoryView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
        })), 
      
      # ===================== TEATMENT ===========================================================

  path('treatment',   TreatmentView.as_view({
        'get':'list',
        'post':'create'
        })), 
  path('treatment/<str:pk>',   TreatmentView.as_view({
        'delete':'destroy',
        'patch':'partial_update',
        'get':'retrieve'
        })), 

      # ===================== DISEASE ===========================================================

  path('disease', DiseaseView.as_view({
        'post':'create_in_builk_or_single',
        'get':'list'
    })),
  path('disease/<str:pk>', DiseaseView.as_view({
        'delete':'destroy',
        'patch':'partial_update'
    })),

      # ===================== DATA EXTRACTION ===========================================================

  path('dataExctraction',   DataExcraction.as_view({
        'get':'retrieve',
        })), 

      # ===================== DATA EXTRACTION PREPROCESSING DISEASE ===========================================================

  path('doctorRecommendatinExtraction',   DataExcraction.as_view({
        'get':'extract_dataset_doctor_recommendation',
        })),
  path('desiasePrediction', views.desiasePrediction, name='desiasePrediction'),
  path('setting_page', views.setting_page, name='setting_page'),
]
