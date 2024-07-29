from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from ..utils.utils import *
from django.conf import settings
from Main_app.models import *
from sklearn.svm import SVC
from datetime import date
import pandas as pd
import pickle
import os


modelling = settings.STATICFILES_DIRS[0] + r'/modelling/'
dataset = settings.STATICFILES_DIRS[0] + r'/dataset'

def dataExtractionPreprocessingDisease():
    x_columns = ['PatientHpi', 'PhysicalExamination', 'Age', 'BodyTemperature', 'SPO2',
    'Occupation', 'NormalPulse', 'SystolicBloodPressure',
    'DiastolicBloodPressure', 'BMI', 'Location', 'Gender', 'TargetGroup',
    'RespiratoryRate']
    
    data_dictionary = {}
    for column in x_columns:
        data_dictionary[column] = []

    all_patient_data = PatientDetail.objects.all()
    for patient in all_patient_data:
        data_dictionary['PatientHpi'].append(patient.patient_hpi)
        data_dictionary['PhysicalExamination'].append(patient.physical_examination)
        data_dictionary['Age'].append(patient.age)
        data_dictionary['BodyTemperature'].append(patient.body_temperature)
        data_dictionary['SPO2'].append(patient.spo2)
        data_dictionary['Occupation'].append(patient.occupation)
        data_dictionary['NormalPulse'].append(patient.normal_pulse)
        data_dictionary['SystolicBloodPressure'].append(patient.systolic_blood_pressure)
        data_dictionary['DiastolicBloodPressure'].append(patient.diastolic_blood_pressure)
        data_dictionary['BMI'].append(patient.bmi)
        data_dictionary['Location'].append(patient.location)
        data_dictionary['Gender'].append(patient.gender)
        data_dictionary['TargetGroup'].append(patient.target_group)
        data_dictionary['RespiratoryRate'].append(patient.respiratory_rate)
    
    new_dataset_from_db = pd.DataFrame(data_dictionary)
    file_name = dataset + '/dataset.csv'
    new_dataset_from_db.to_csv(file_name)
    
def startTraining():
    """
    traininh and performing data 
    """
    print("start Training model")
    dataExtractionPreprocessingDisease()
    all_files = os.listdir(dataset)
    arr_data = []
    for file in all_files:
        data_individual = pd.read_csv(dataset + '/' + file)
        arr_data.append(data_individual)
    df = pd.concat(arr_data, ignore_index=True)
    df.drop_duplicates(inplace=True)
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

    y = df.Disease
    x = df.drop('Disease', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    classifiers = [
        RandomForestClassifier(),
        GradientBoostingClassifier(),
        SVC(),
        LogisticRegression(),
        DecisionTreeClassifier(),
        GaussianNB(),
        KNeighborsClassifier(),

    ]

    best_accuracy = 0
    best_model = None
    recall = 0
    precision = 0

    for classifier in classifiers:
        classifier.fit(X_train_scaled, y_train)
        y_pred = classifier.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)


        print(f"{classifier.__class__.__name__} Accuracy: {accuracy}")

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = classifier
            precision = precision_score(y_test, y_pred, average='weighted')
            recall = recall_score(y_test, y_pred, average='weighted')

    model_filename = modelling + 'model of ' + str(date.today()) + '.pkl'
    with open(model_filename, 'wb') as file:
        pickle.dump(best_model, file)  
    
        ModelTrainingResult.objects.get_or_create(model_name = classifier.__class__.__name__, model_file = model_filename, accuracy = best_accuracy, precision = precision, recall = recall)