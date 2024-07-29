import pickle
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
import google.generativeai as genai
from rest_framework import status
from Main_app.Validators import *
from Main_app.serializers import *
from Main_app.models import *
from Main_app.utils import *
from transformers import pipeline
import pandas as pd
import joblib

transformer_model_pipe = pipeline("text-classification", model="shanover/symps_disease_bert_v3_c41")

def initilize(request):
    upload_diseases(request)
    return Response("initilized", status=status.HTTP_200_OK)


def desiasePrediction(request):
    if request.method == 'POST':
        x_columns = ['PatientHpi', 'PhysicalExamination', 'Age', 'BodyTemperature', 'SPO2',
    'Occupation', 'NormalPulse', 'SystolicBloodPressure',
    'DiastolicBloodPressure', 'BMI', 'Location', 'Gender', 'TargetGroup',
    'RespiratoryRate']
        
        prediction_range = -1
        fully_patient_detail = ''
        data_dictionary = {}
        for column in x_columns:
            data_dictionary[column] = []
        
        data = request.POST
        height = 40
        weight = 10

        general_exam = data.get('GeneralExam', '')
        abdominal_exam = data.get('abdominal_exam', '')
        neurological_exam = data.get('neurological_exam', '')
        other_finding = data.get('other_finding', '')
        
        physical_examination = general_exam +" " + abdominal_exam  +" "+ neurological_exam  +" "+ other_finding
        data_dictionary['PhysicalExamination'].append(physical_examination)
        
        main_symptoms = data.get('main_symptoms', '')
        
        associated_symptoms = data.get('associated_symptoms', '')
        
        additional_info = data.get('additional_info', '')
        
        patient_hpi = main_symptoms  +" "+ associated_symptoms  +" "+ additional_info
        
        fully_patient_detail += "main syptoms: " + main_symptoms + " associated_symptoms: " + associated_symptoms + " additional_info: " + additional_info
        
        fully_patient_detail +=" " + 'Physical Examination: 1. General Exam:' + general_exam + ' 2. Abdominal Exam:' + abdominal_exam + ' 3. Neurological Exam:' + neurological_exam + ' 4. Other Finding:' + other_finding
        
        data_dictionary['PatientHpi'].append(patient_hpi)
        
        general_sentence = patient_hpi + " " + physical_examination
        
        model_prediction = transformer_model_pipe(general_sentence)

        prediction_status = False
        disease_arr = ["(Vertigo) Paroxysmal Positional Vertigo", "AIDS", "Acne", "Alcoholic hepatitis", "Allergy", "Arthritis", "Bronchial Asthma", "Cervical spondylosis", "Chicken pox", "Chronic cholestasis", "Common Cold", "Dengue", "Diabetes", "Dimorphic hemorrhoids (piles)", "Drug Reaction", "Fungal infection", "GERD", "Gastroenteritis", "Heart attack", "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E", "Hypertension", "Hyperthyroidism", "Hypoglycemia", "Hypothyroidism", "Impetigo", "Jaundice", "Malaria", "Migraine", "Osteoarthritis", "Paralysis (brain hemorrhage)", "Peptic ulcer disease", "Pneumonia", "Psoriasis", "Tuberculosis", "Typhoid", "Urinary tract infection", "Varicose veins", "Hepatitis A"]
        output_dict = {"main":[], "differential":[]}

        for model_predicted in model_prediction:
            disease_predicted = model_predicted['label']
            diseease_id =int(disease_predicted[6:])
            if model_predicted['score'] >=0.5:
                pediction_status = True
                output_dict['main'].append(disease_arr[diseease_id])
            else:
                output_dict['differential'].append(disease_arr[diseease_id])
                
        if not prediction_status:
            if data.get('Age', None):
                age = int(data.get('Age'))
                target_group = ''
                if data.get('TargetGroup', None):
                    target_group = data.get('TargetGroup')
                else:
                    if age <18:
                        target_group = "Children"
                    elif age >=18 and age <= 50:
                        target_group = "Young"
                    elif age >50 and age <= 60:
                        target_group = "Mild Youth"
                    else:
                        target_group = "Elders"
                data_dictionary['TargetGroup'].append(target_group)
                data_dictionary['Age'].append(age)

            else:
                return Response({'message': 'Age is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            fully_patient_detail += " Age: " + str(age) + " patient belongs to group of  " + target_group

            if data.get('BodyTemperature', None):
                data_dictionary['BodyTemperature'].append(float(data.get('BodyTemperature')))
                fully_patient_detail += " Body Temperature: " + str(float(data.get('BodyTemperature')))
            else:
                return Response({'message': 'BodyTemperature is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            if data.get('NormalPulse', None):
                data_dictionary['NormalPulse'].append(int(data.get('NormalPulse')))
                fully_patient_detail += " Normal Pulse: " + str(int(data.get('NormalPulse')))
            else:
                return Response({'message': 'NormalPulse is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            if data.get('SystolicBloodPressure', None):
                fully_patient_detail += " Systolic Blood Pressure: " + str(int(data.get('SystolicBloodPressure')))
                data_dictionary['SystolicBloodPressure'].append(int(data.get('SystolicBloodPressure')))
            else:
                return Response({'message': 'Systolic Blood Pressure is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            if data.get('DiastolicBloodPressure', None):
                fully_patient_detail += " Diastolic Blood Pressure: " + str(int(data.get('DiastolicBloodPressure')))
                data_dictionary['DiastolicBloodPressure'].append(int(data.get('DiastolicBloodPressure')))
            else:
                return Response({'message': 'Diastolic Blood Pressure is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            if data.get('Location', None):
                fully_patient_detail += " Location: " + str(data.get('Location'))
                data_dictionary['Location'].append(data.get('Location'))
            else:
                return Response({'message': 'Location is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            if data.get('weights', None):
                fully_patient_detail += " Weight: " + str(int(data.get('weights')))
                weight = int(data.get('weights'))

            else:
                return Response({'message': 'Weight is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            if data.get('heights', None):
                fully_patient_detail += " Height: " + str(int(data.get('heights')))
                height = int(data.get('heights'))
                
            else:
                return Response({'message': 'Height is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            bmi_value = weight/(height*height)
            data_dictionary['BMI'].append(bmi_value)
            fully_patient_detail += " BMI: " + str(bmi_value)
            
            if data.get('Gender', None):
                fully_patient_detail += " Gender: " + str(data.get('Gender'))
                gender = 0
                if data.get('Gender') == 'Male':
                    gender = 1
                elif data.get('Gender') == 'Female':
                    gender = 0
                data_dictionary['Gender'].append(gender)
            else:
                return Response({'message': 'Gender is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            spo2_value = 100
            if data.get('SPO2', None):
                fully_patient_detail += " SPO2: " + str(float(data.get('SPO2')))
                spo2_value = float(data.get('SPO2'))

            data_dictionary['SPO2'].append(spo2_value)
            
            Occupation = data.get('Occupation', None)
            if Occupation:
                data_dictionary['Occupation'].append(Occupation)
            else:
                data_dictionary['Occupation'].append('Unknown')
            
            fully_patient_detail += " Occupation: " + str(Occupation)
            
            if data.get('RespiratoryRate', None):
                fully_patient_detail += " Respiratory Rate: " + str(float(data.get('RespiratoryRate')))
                data_dictionary['RespiratoryRate'].append(float(data.get('RespiratoryRate')))
            else:
                return Response({'message': 'Respiratory Rate is required'}, status=status.HTTP_400_BAD_REQUEST)
            
            for key, value in data_dictionary.items():
                print("key : ", key, "maximum number : ", len(value))
                
            main_symptoms_list = []
            associated_symptoms_list = []
            
            if data.get('main_symptoms', []):
                main_symptoms = data.get('main_symptoms')    
                try:
                    main_symptoms_list = main_symptoms.split(',')
                except Exception as e:
                    main_symptoms_list = [main_symptoms]
            
            if data.get('associated_symptoms', None):
                associated_symptoms = data.get('associated_symptoms')
                try:
                    associated_symptoms_list = associated_symptoms.split(',')
                except Exception as e:
                    associated_symptoms_list = associated_symptoms

            if True:
                genai.configure(api_key='AIzaSyCzvsGqemdf25EVXvWKy4qN18arGMGn6Y0')
                ai_model = genai.GenerativeModel('gemini-pro')

                response = ai_model.generate_content(f"based tretment guideline found in previous chats and tanzania treatment guidelines. predict patiet disease based on this information {fully_patient_detail} i need only name of disease and differential disease if any i dont need more explanation")
                print(response.text)
                      
                main_disease, differential_diseases = extract_disease_and_differential(response.text)
                output_dict["main"].append(main_disease)  
                        
                print("\n\n\n\n\n\n\n\n")
                print('result from geminia API')
                print(output_dict)
                print("\n\n\n\n\n\n\n\n")
                prediction_range = -1
                if main_disease or differential_diseases:
                    for diff_disease in differential_diseases:
                        prediction_range = -1
                        output_dict["differential"].append(diff_disease)
                      
            df = pd.DataFrame(data_dictionary)
            df['PatientHpi'] = df['PatientHpi'].apply(preprocess_text)
            df['PhysicalExamination'] = df['PhysicalExamination'].apply(preprocess_text)
            df['Gender'] = df['Gender'].apply(preprocess_text)
            df['TargetGroup'] = df['TargetGroup'].apply(preprocess_text)
            df['Occupation'] = df['Occupation'].apply(preprocess_text)
            df['Location'] = df['Location'].apply(preprocess_text)

            df['PatientHpi'] = df['PatientHpi'].apply(lambda x: get_vectors(x, word2vec_model))
            df['PhysicalExamination'] = df['PhysicalExamination'].apply(lambda x: get_vectors(x, word2vec_model))
            df['Gender'] = df['Gender'].apply(lambda x: get_vectors(x, word2vec_model))
            df['TargetGroup'] = df['TargetGroup'].apply(lambda x: get_vectors(x, word2vec_model))
            df['Occupation'] = df['Occupation'].apply(lambda x: get_vectors(x, word2vec_model))
            df['Location'] = df['Location'].apply(lambda x: get_vectors(x, word2vec_model))
            
            df['PatientHpi'] = df['PatientHpi'].apply(lambda x: aggregate_vectors(x))
            df['PhysicalExamination'] = df['PhysicalExamination'].apply(lambda x: aggregate_vectors(x))
            df['Gender'] = df['Gender'].apply(lambda x: aggregate_vectors(x))
            df['TargetGroup'] = df['TargetGroup'].apply(lambda x: aggregate_vectors(x))
            df['Occupation'] = df['Occupation'].apply(lambda x: aggregate_vectors(x))
            df['Location'] = df['Location'].apply(lambda x: aggregate_vectors(x))
            
            model = joblib.load(modelling)
            prediction = model.predict(df)
            disease_mapping = {0: 'Pneumonia', 1: 'Normal', 2: 'Diabates', 3: 'UTI', 4: 'Typhoid'}          

            for value in prediction:
                output_dict['main'].append(disease_mapping[value])
  
        patient_data = PatientDetail.objects.get_or_create(
            main_symptoms=[data.get('main_symptoms')],
            associated_symptoms=[data.get('associated_symptoms')],
            patient_hpi= patient_hpi,
            physical_examination=physical_examination,
            age=data.get('Age', None),
            body_temperature=data.get('BodyTemperature', None),
            spo2=data.get('SPO2', 100),
            occupation=data.get('Occupation', 'Farmer'),
            normal_pulse=data.get('NormalPulse', None),
            systolic_blood_pressure=data.get('SystolicBloodPressure', 120),
            diastolic_blood_pressure=data.get('DiastolicBloodPressure', 80),
            bmi=int(data.get('heights'))/(int(data.get("weights"))**2),
            location=data.get('Location', None),
            gender=data.get('Gender', None),
            target_group=data.get('TargetGroup', None),
            respiratory_rate=data.get('RespiratoryRate', 12),
            diseases = [output_dict])
        # serializer = PatientDetailSerializer(patient_data[0])
            
        context = {'disease': output_dict}
        return render(request, 'index.html', context)

    return render(request, 'index.html')

def setting_page(request):
    return render(request, 'index.html')
