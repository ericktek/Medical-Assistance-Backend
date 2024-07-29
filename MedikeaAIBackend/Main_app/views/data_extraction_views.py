from drf_spectacular.utils import extend_schema
import pandas as pd
import requests
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from Main_app.serializers import *
from Main_app.models import *
from datetime import date

class DataExcraction(ViewSet):
    def retrieve(self,request):
        data_dictionary ={'patient':[], 'Longitude':[], 'latitude':[], 'occupaton':[], 'gender':[], 'Age':[], 'symptoms':[]}

        records = Record.objects.all()
        for record in records:
            patient_id = record.patient_id
            longitude = record.longitude
            latitude = record.latitude
            occupation = record.patient_id.occupation
            gender = record.patient_id.gender
            today = date.today()
            age = today.year - record.patient_id.date_birth.year - ((today.month, today.day) < (record.patient_id.date_birth.month, record.patient_id.date_birth.day))
            sympton = ''
            symptoms_json = record.symptoms
            for symptom in symptoms_json:
                sympton += symptom.machine_learning_value + '00'
            data_dictionary['patient'].append(patient_id)
            data_dictionary['Longitude'].append(longitude)
            data_dictionary['latitude'].append(latitude)
            data_dictionary['occupaton'].append(occupation)
            data_dictionary['Age'].append(age)
            data_dictionary['gender'].append(gender)
            data_dictionary['symptoms'].append(int(sympton))
        
        data = pd.DataFrame(data_dictionary)
        dateset_at = dataset + r'dataset of ' + str(date.today()) + '.csv'
        data.to_csv(dateset_at, index=False)
        return Response(data_dictionary, status=status.HTTP_200_OK)
    
    def extract_dataset_doctor_recommendation(self, request):
        complete_visit_url = visit_url + r'dataExtract'
        complete_sso_url = sso_url + r'extract'
        data_retrieved = requests.get(complete_visit_url)
        data_retrieved = data_retrieved.json()
        
        patient_doctor_data = requests.get(complete_sso_url)
        recieved_patient_doctor = patient_doctor_data.json() 

        data_dict = {'patient_id':[], 'doctor_id':[], 'visit_type':[], 'reason':[], 'patientAge':[], 'patientGender':[], 'consultation_date':[], 'DoctorGender':[], 'designation':[], 'Specialist':[], 'Slot':[], 'symptoms':[]}
        for data in data_retrieved:
            for visit in data['visit']:
                patient_age = 0
                patient_gender = ''
                doctor_gender = ''
                doctor_designation = ''
                doctor_specialist = ''

                if recieved_patient_doctor['patients']:
                    for patient in recieved_patient_doctor['patients']:
                            if patient['id'] == visit['patient_id']:
                                age =date.today().year - patient['date_birth'].year -patient['date_birth'].year
                                gender = patient['gender']
                                patient_age = age
                                patient_gender = gender

                if recieved_patient_doctor['doctors']:
                    for doctor in recieved_patient_doctor['doctors']:
                            if doctor['id'] == visit['doctor_id']:
                                gender = doctor['gender']
                                designation = doctor['designation']
                                specialist = doctor['specialist']
                                doctor_gender = gender
                                doctor_designation = designation
                                doctor_specialist = specialist
                data_dict['patientAge'].append(patient_age)
                data_dict['patientGender'].append(patient_gender)
                data_dict['designation'].append(doctor_designation)
                data_dict['Specialist'].append(doctor_specialist)

                data_dict['Slot'].append(visit['slot']) 
                data_dict['patient_id'].append(visit['patient_id'])
                data_dict['doctor_id'].append(visit['doctor_id'])
                data_dict['visit_type'].append(visit['visit_type'])
                data_dict['consultation_date'].append(visit['date'])
                data_dict['reason'].append(visit['reason'])
                data_dict['symptoms'].append(visit['symptoms'])
        
        return Response(data_dict, status=status.HTTP_200_OK)
