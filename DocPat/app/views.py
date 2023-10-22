from django.shortcuts import render
from django.http import HttpResponse

from . import utils

# Create your views here.

def index(request):
    return render(request, "index.html")

def doctor(request):
    if request.method == "POST":
        doc_id = request.POST['doc_id']
        password = request.POST['password']
        if doc_id in utils.list_doc_id():
            if password == utils.get_doc_pass(doc_id):
                return render(request, "doctor_appointment.html", {
                    "doc_name" : utils.get_doc_name(doc_id)
                })
            else:
                return render(request, "doctor.html", {
                    "error" : """
                        <div id='error_box'>
                            ❌ Wrong Credentials
                        </div>
                    """})
        else:
            return render(request, "doctor.html", {
                "error" : """
                    <div id='error_box'>
                        ❌ Wrong Credentials
                    </div>
                """})
    else:
        return render(request, "doctor.html")
    
def patient(request):
    if request.method == "POST":
        Operation = request.POST['Operation']

        if Operation == "book_new":
            return render(request, "patient_appointment_new.html")
        
        elif Operation == "login":
            patient_id = request.POST['patient_id']
            password = request.POST['password']
            if patient_id in utils.list_patient_id():
                if password == utils.get_patient_pass(patient_id):
                    appointments = utils.get_patient_appointment(patient_id)
                    COUNT = len(appointments)
                    entries = []
                    for appointment in appointments:  
                        entries.append(f"<td>{ appointment['time'] }</td><td>{ appointment['condition'] }</td><td>{ appointment['doctor'] }</td>" )

                    return render(request, "patient_appointment.html",{
                        "range_count" : range(1, COUNT+1),
                        "entries" : entries
                    })
                else:
                    return render(request, "patient.html", {
                        "error" : """
                            <div id='error_box'>
                                ❌ Wrong Credentials
                            </div>
                        """})
            else:
                return render(request, "patient.html", {
                    "error" : """
                        <div id='error_box'>
                            ❌ Wrong Credentials
                        </div>
                    """})

        elif Operation == "cancel":
            print('you pressed cancel')
    else:
        return render(request, "patient.html")

def patient_new(request):
    if request.method == "POST":
        return render(request, "patient_new.html")
    else:
        return render(request, "patient.html")