import pandas as pd
import requests
from django.conf import settings
from ..models import *

def UpdatingMachineLearningValues():
    diseases = Disease.objects.all()
    for index, disease in enumerate:
        disease.machine_learning_value = index
        disease.save()

def upload_diseases(request):
    treatment_url = 'http://' + request.get_host() + '/api/v1/medicalasistant/treatment'

    disease_url = settings.STATICFILES_DIRS[0] + r'/dataset/more-Extracted-data.csv' # Path to the model
    df = pd.read_csv(disease_url)

    symptoms_DICT = {}
    symptoms = df['Clinical Presentation'].unique()
    symptoms_number = 0
    for symptom_need_processing in symptoms:
        print(symptom_need_processing)
        try:
            for index, symptom in symptom_need_processing.split(','):
                symptoms_DICT[symptom.strip()] = symptoms_number+ index
        except:
            symptoms_DICT[symptom_need_processing] = symptoms_number
        symptoms_number += 1
    for name, machine_learning_value in symptoms_DICT.items():
        Symptom.objects.get_or_create(name=name, machine_learning_value=machine_learning_value)

    diseases = df['Disease'].unique()
    diseases_DICT = {}
    for index, disease in enumerate(diseases):
        diseases_DICT[disease.strip()] = index
    for name, machine_learning_value in diseases_DICT.items():
        disease_exist = Disease.objects.filter(name=name).exists()
        if not disease_exist:
            Disease.objects.create(name=name, machine_learning_value=machine_learning_value)
        else:
            disease = Disease.objects.get(name=name)
            disease.machine_learning_value = machine_learning_value
            disease.save()
            
    clinical_presentations = set(df['Clinical Presentation'].tolist())
    clinical_presentations_DICT = {}
    for index1, clinical_presentation_arr in enumerate(clinical_presentations):
        for index, clinical_presentation in enumerate(clinical_presentation_arr.split(',')):
            clinical_presentations_DICT[clinical_presentation.strip()] = index
    for name, machine_learning_value in clinical_presentations_DICT.items():
        clinical_presentation_exist = Symptom.objects.filter(name=name).exists()
        if not clinical_presentation_exist:
            Symptom.objects.create(name=name, machine_learning_value=machine_learning_value)
        else:
            clinical_presentation = Symptom.objects.filter(name=name)
            clinical_presentation.update(machine_learning_value = machine_learning_value)

    treatment_category = ['Pharmacological Treatment', 'Non-Pharmacological Treatment', 'Other Treatment']
    for name in treatment_category:
        category = TeatmentCategory.objects.get_or_create(name=name)
        category_list = df[name].tolist()
        treatments_arr = []
        for index, treatment in enumerate(category_list):

            disease_obj = Disease.objects.filter(name=df['Disease'][index])
            treatement_arr = []
            try:
                treatments = treatment.split('-')
                for treat in treatments:
                    treatement_json = {}
                    treatement_obj = Treatment.objects.get_or_create(name=treat.strip(), category=category[0])
                    treatement_url = 'http://' + request.get_host() + '/api/v1/medicalasistant/treatment/' + str(treatement_obj[0].id)
                    try:
                        treatement_json = requests.get(treatement_url).json()
                    except:
                        pass
                treatement_obj.append(treatement_json)
            
            except:
                treatement_obj = Treatment.objects.get_or_create(name=treatment.strip(), category=category[0])
                treatement_url = 'http://' + request.get_host() + '/api/v1/medicalasistant/treatment/' + str(treatement_obj[0].id)
                try:
                    treatement_json = requests.get(treatement_url).json()
                except:
                    pass
                treatement_arr.append(treatement_json)
            
            symptom_current = df['Clinical Presentation'][index]
            symptoms_arr_item_json= []
            try:
                symptoms_arr_item = symptom_current.split(',')
                for symptom_individual in symptoms_arr_item:
                    symptom_obj =symptom_obj = Symptom.objects.get(name=symptom_individual.strip())
                    response = requests.get('http://' + request.get_host() + '/api/v1/medicalasistant/symptom/' + str(symptom_obj.id))
                    symptom_json = response.json()
                    symptoms_arr_item_json.append(symptom_json)
            except:
                symptom_obj = Symptom.objects.get(name=symptom_current.strip())
                response = requests.get('http://' + request.get_host() + '/api/v1/medicalasistant/symptom/' + str(symptom_obj.id))
                symptom_json = response.json()
                symptoms_arr_item_json.append(symptom_json)

            preventations = df['Prevention'][index]

            disease_obj.update(treatment=treatement_arr, prevention=preventations, symptoms=symptoms_arr_item_json)
    
    return True

def upload_symptoms(request):
    medicalasistant_url = 'http://' + request.get_host() + '/api/v1/medicalasistant/symptom'
    data = requests.get(medicalasistant_url).json()
