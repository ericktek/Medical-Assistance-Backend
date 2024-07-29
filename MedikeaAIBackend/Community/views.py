from rest_framework import generics
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from Main_app.models import *
from Main_app.serializers.serializers import *


class OccupationViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer
    
    @extend_schema(
        tags=["Occupation"],
        summary="List all Occupations",
        description="List all Occupations",
        responses={
            200:OccupationSerializer, 400:{"message": "Permission denied"}
        }
        )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @extend_schema(
        tags="Occupation",
        summary="Create Occupation",
        description="Create Occupation",
        request=OccupationSerializer,
        responses={
            200:OccupationSerializer, 400:{"message": "Permission denied"}
        }
        )
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class OccupationDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer

    @extend_schema(
        tags="Occupation",
        summary="Retrieve Occupation",
        description="Retrieve Occupation by using id",
        responses={
            200:OccupationSerializer, 400:{"message": "Permission denied"}
        }
        )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    @extend_schema(
        tags="Occupation",
        summary="update ocupation by using id",
        description="updating ocupation by id",
        request=OccupationSerializer,
        responses={
            200:OccupationSerializer, 400:{"message": "Permission denied"}
        }
    )
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    @extend_schema(
        tags="Occupation",
        summary="delete ocupation by using id",
        description="deleting ocupation by id",
        responses={
            200:OccupationSerializer, 400:{"message": "Permission denied"}
        }
    )
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class SymptomViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    
    @extend_schema(
        tags=["Symptom"],
        summary="List all Symptoms",
        description="List all Symptoms",
        responses={
            200:SymptomSerializer, 400: {"message": "Permission denied"}
        }
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
    @extend_schema(
        tags="Symptom",
        summary="Create Symptom",
        description="Create Symptom",
        request=SymptomSerializer,
        responses={
            200:SymptomSerializer, 400: {"message": "Permission denied"}
        }
    )
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class SymptomDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
    
    @extend_schema(
        tags="Symptom",
        summary="Retrieve Symptom",
        description="Retrieve Symptom by using id",
        responses={
            200:SymptomSerializer, 400: {"message": "Permission denied"}
        }
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    @extend_schema(
        tags="Symptom",
        summary="update symptom by using id",
        description="updating symptom by id",
        request=SymptomSerializer,
        responses={
            200:SymptomSerializer, 400: {"message": "Permission denied"}
        }
        )
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    @extend_schema(
        tags="Symptom",
        summary="delete symptom by using id",
        description="deleting symptom by id",
        responses={
            200:SymptomSerializer, 400: {"message": "Permission denied"}
        }
        )
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class SpecialityViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    
    @extend_schema(
        tags=["Speciality"],
        summary="List all Specialities",
        description="List all Specialities",
        responses={
            200:SpecialitySerializer, 400: {"message": "Permission denied"}
        }
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @extend_schema(
        tags="Speciality",
        summary="Create Speciality",
        description="Create Speciality",
        request=SpecialitySerializer,
        responses={
            200:SpecialitySerializer, 400: {"message": "Permission denied"}
        }
    )
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class SpecialityDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

    @extend_schema(
        tags="Speciality",
        summary="Retrieve Speciality",
        description="Retrieve Speciality by using id",
        responses={
            200:SpecialitySerializer, 400: {"message": "Permission denied"}
        }
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    @extend_schema(
        tags="Speciality",
        summary="Retrieve Speciality",
        description="Retrieve Speciality by using id",
        responses={
            200: SpecialitySerializer, 400: {"message": "Permission denied"}
            }
    )
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class HospitalViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class HospitalDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class CommunityViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class CommunityDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class DoctorProfileViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class DoctorProfileDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class DrugstoreViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Drugstore.objects.all()
    serializer_class = DrugstoreSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class DrugstoreDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Drugstore.objects.all()
    serializer_class = DrugstoreSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class TeatmentCategoryViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = TeatmentCategory.objects.all()
    serializer_class = TeatmentCategorySerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class TeatmentCategoryDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = TeatmentCategory.objects.all()
    serializer_class = TeatmentCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class TreatmentViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class TreatmentDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class PharmacologicalTreatmentViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = PharmacologicalTreatment.objects.all()
    serializer_class = PharmacologicalTreatmentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class PharmacologicalTreatmentDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = PharmacologicalTreatment.objects.all()
    serializer_class = PharmacologicalTreatmentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class DiseasePreventionViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = DiseasePrevention.objects.all()
    serializer_class = DiseasePreventionSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class DiseasePreventionDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = DiseasePrevention.objects.all()
    serializer_class = DiseasePreventionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class DifferentialDiagnosisCategoryViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = DifferentialDiagnosisCategory.objects.all()
    serializer_class = DifferentialDiagnosisCategorySerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class DifferentialDiagnosisCategoryDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = DifferentialDiagnosisCategory.objects.all()
    serializer_class = DifferentialDiagnosisCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class DifferentialDiagnosisViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = DifferentialDiagnosis.objects.all()
    serializer_class = DifferentialDiagnosisSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class DifferentialDiagnosisDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = DifferentialDiagnosis.objects.all()
    serializer_class = DifferentialDiagnosisSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class InvestigationViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Investigation.objects.all()
    serializer_class = InvestigationSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class InvestigationDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Investigation.objects.all()
    serializer_class = InvestigationSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class DiseaseViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class DiseaseDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class ModelTrainingResultViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = ModelTrainingResult.objects.all()
    serializer_class = ModelTrainingResultSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class ModelTrainingResultDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = ModelTrainingResult.objects.all()
    serializer_class = ModelTrainingResultSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class MessageViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class MessageDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class PostViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class PostDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class CommentViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class CommentDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class LikeViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class LikeDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class CaseViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class CaseDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class ResourceViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class ResourceDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)

class PatientDetailViewSet(generics.GenericAPIView,
                   ListModelMixin, CreateModelMixin):
    queryset = PatientDetail.objects.all()
    serializer_class = PatientDetailSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)

class PatientDetailDetailViewSet(generics.GenericAPIView,
                   RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = PatientDetail.objects.all()
    serializer_class = PatientDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)
