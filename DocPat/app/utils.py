import csv
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def list_doc_id():
    doc_ids = []
    with default_storage.open('data/doctor.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            doc_id = row.get('Doc_ID')
            if doc_id:
                doc_ids.append(doc_id)
    return doc_ids

def list_patient_id():
    patient_ids = []
    with default_storage.open('data/patient.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            patient_id = row.get('Patient_ID')
            if patient_id:
                patient_ids.append(patient_id)
    return patient_ids

def list_doc():
    doc_ids = []
    with default_storage.open('data/doctor.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            doc_id = row.get('Doc_ID')
            if doc_id:
                doc_ids.append(doc_id)
    return None

def get_doc_pass(target_doc_id):
    with open('data/doctor.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            doc_id = row.get('Doc_ID')
            if doc_id == target_doc_id:
                return row.get('Password')
            
def get_doc_name(target_doc_id):
    with open('data/doctor.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            doc_id = row.get('Doc_ID')
            if doc_id == target_doc_id:
                return row.get('Name')

def get_patient_pass(target_patient_id):
    with open('data/patient.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            patient_id = row.get('Patient_ID')
            if patient_id == target_patient_id:
                return row.get('Password')
                 
def get_patient_appointment(target_doc_id):
    appointments = []
    
    with open(f"data/patients/{target_doc_id}.csv", 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
   
        for row in csv_reader:
            
            appointment = {
                'time': row['Time'],
                'condition': row['Condition'],
                'doctor': row['Doctor'],
            }

            appointments.append(appointment)

    return appointments