from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('occupation', OccupationViewSet.as_view(), name='Occupation'),
    path('occupation/<str:pk>', OccupationDetailViewSet.as_view(), name='Occupation'),
    
    path('symptom', SymptomViewSet.as_view(), name='Symptom'),
    path('symptom/<str:pk>', SymptomDetailViewSet.as_view(), name='Symptom'),
    
    path('speciality', SpecialityViewSet.as_view(), name='Speciality'),
    path('speciality/<str:pk>', SpecialityDetailViewSet.as_view(), name='Speciality'),
    
    path('hospital', HospitalViewSet.as_view(), name='Hospital'),
    path('hospital/<str:pk>', HospitalDetailViewSet.as_view(), name='Hospital'),
    
    path('community', CommunityViewSet.as_view(), name='Community'),
    path('community/<str:pk>', CommunityDetailViewSet.as_view(), name='community'),
    
    path('doctor/profile', DoctorProfileViewSet.as_view(), name='DoctorProfile'),
    path('doctor/profile/<str:pk>', DoctorProfileDetailViewSet.as_view(), name='DoctorProfile'),
    
    path('prescription', DrugstoreViewSet.as_view(), name='Prescription'),
    path('prescription/<str:pk>', DrugstoreDetailViewSet.as_view(), name='Prescription'),
    
    path('treatment/category', TeatmentCategoryViewSet.as_view(), name='TreatmentCategory'),
    path('treatment/category/<str:pk>', TeatmentCategoryDetailViewSet.as_view(), name='TreatmentCategory'),
    
    path('treatment', TreatmentViewSet.as_view(), name='Treatment'),
    path('treatment/<str:pk>', TreatmentDetailViewSet.as_view(), name='Treatment'),
    
    path('pharmacological/treatment', PharmacologicalTreatmentViewSet.as_view(), name='PharmacologicalTreatment'),
    path('pharmacological/treatment/<str:pk>', PharmacologicalTreatmentDetailViewSet.as_view(), name='PharmacologicalTreatment'),
    
    path('disease/prevention', DiseasePreventionViewSet.as_view(), name='DiseasePrevention'),
    path('disease/prevention/<str:pk>', DiseasePreventionDetailViewSet.as_view(), name='DiseasePrevention'),
    
    path('differential/diagnosis/category', DifferentialDiagnosisCategoryViewSet.as_view(), name='DifferentialDiagnosisCategory'),
    path('differential/diagnosis/category/<str:pk>', DifferentialDiagnosisCategoryDetailViewSet.as_view(), name='DifferentialDiagnosisCategory'),
    
    path('differential/diagnosis', DiseasePreventionViewSet.as_view(), name='DifferentialDiagnosis'),
    path('differential/diagnosis/<str:pk>', DifferentialDiagnosisDetailViewSet.as_view(), name='DifferentialDiagnosis'),
    
    path('investigation', InvestigationViewSet.as_view(), name='Investigation'),
    path('investigation/<str:pk>', InvestigationDetailViewSet.as_view(), name='Investigation'),
    
    path('disease', DiseaseViewSet.as_view(), name='Disease'),
    path('disease/<str:pk>', DiseaseDetailViewSet.as_view(), name='Disease'),
    
    path('model/training/result', ModelTrainingResultViewSet.as_view(), name='ModelTrainingResult'),
    path('model/training/result/<str:pk>', ModelTrainingResultDetailViewSet.as_view(), name='ModelTrainingResult'),

    path('message', MessageViewSet.as_view(), name='Message'),
    path('message/<str:pk>', MessageDetailViewSet.as_view(), name='Message'),
    
    path('post', PostViewSet.as_view(), name='Post'),
    path('post/<str:pk>', PostDetailViewSet.as_view(), name='Post'),
    
    path('comment', CommentViewSet.as_view(), name='Comment'),
    path('comment/<str:pk>', CommentDetailViewSet.as_view(), name='Comment'),
    
    path('Like', LikeViewSet.as_view(), name='Like'),
    path('like/<str:pk>', LikeDetailViewSet.as_view(), name='Like'),
    
    path('case', CaseViewSet.as_view(), name='Case'),
    path('case/<str:pk>', CaseDetailViewSet.as_view(), name='Case'),
    
    path('resource', ResourceViewSet.as_view(), name='Resource'),
    path('resource/<str:pk>', ResourceDetailViewSet.as_view(), name='Resource'),
    
    
]