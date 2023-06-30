from django.shortcuts import render, redirect
from .models import Clinic, Doctor, Visit
from .forms import VisitForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateClinicForm


@login_required
def dashboard(request):
    clinics = Clinic.objects.filter(user=request.user)
    doctors = Doctor.objects.filter(user=request.user)
    visits = Visit.objects.filter(user=request.user)
    if request.method == 'POST':
        form = CreateClinicForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateClinicForm()

    return render(request, 'visits/dashboard.html', {'clinics': clinics, 'doctors': doctors, 'visits': visits, 'form': form})


@login_required
def clinics(request):
    clinics = Clinic.objects.filter(user=request.user)
    return render(request, 'visits/clinics.html', {'clinics': clinics})

@login_required
def doctors(request, clinic_id):
    doctors = Doctor.objects.filter(user=request.user, clinic_id=clinic_id)
    return render(request, 'visits/doctors.html', {'doctors': doctors})

@login_required
def visits(request, doctor_id):
    visits = Visit.objects.filter(user=request.user, doctor_id=doctor_id)
    return render(request, 'visits/visits.html', {'visits': visits})

@login_required
def new_visit(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visits')
    else:
        form = VisitForm()
    return render(request, 'visits/new_visit.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'visits/signup.html', {'form': form})
