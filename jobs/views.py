from django.shortcuts import render
from django.db import connection
from .models import *
# Create your views here.
def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def home(request):
    jobs = Job.objects
    summary = Summary.objects
    experience = Experience.objects
    project = Project.objects
    skills = Skill.objects
    awards = Awards.objects
    cursor = connection.cursor()
    try:
        cursor.execute('''SELECT distinct id,cast(DATE_PART('year',jobs_awards.date) as integer) as yr, name  from jobs_awards''')
    finally:
        result = dictfetchall(cursor)
        cursor.close()
    print(result)
    
    return render(request, 'jobs/home.html',{'jobs':jobs, 'summary':summary, 'exp' : experience,'proj' : project, 'skill':skills,'awd_lst':result,'awards':awards})

def home_2(request):
    jobs = Job.objects
    summary = Summary.objects

    return render(request, 'jobs/home_.html',{'jobs':jobs, 'summary':summary})
