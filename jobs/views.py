from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    jobs = Job.objects
    summary = Summary.objects
    print(summary.all)
    experience = Experience.objects
    print(type(experience))
    return render(request, 'jobs/home.html',{'jobs':jobs, 'summary':summary, 'exp' : experience})

def home_2(request):
    jobs = Job.objects
    summary = Summary.objects

    return render(request, 'jobs/home_2.html',{'jobs':jobs, 'summary':summary})
