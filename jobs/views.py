from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    jobs = Job.objects
    summary = Summary.objects
    experience = Experience.objects
    project = Project.objects
    skills = Skill.objects
    awards = Awards.objects
    return render(request, 'jobs/home.html',{'jobs':jobs, 'summary':summary, 'exp' : experience,'proj' : project, 'skill':skills,'awards':awards})

def home_2(request):
    jobs = Job.objects
    summary = Summary.objects

    return render(request, 'jobs/home_.html',{'jobs':jobs, 'summary':summary})
