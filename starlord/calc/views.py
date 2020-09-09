from django.shortcuts import render,redirect
from django.http import HttpResponse
from calc.models import Incident
# Create your views here.

def incident(request):
    return render(request, 'index3.html')

def report(request):
    if request.method=="POST":
        button=request.POST["button"]
        if button=="cancel":
            return redirect('/')
        try:
            env=request.POST["Environmental_Incident"], 
        except:
            env=False
        try:
            i=bool(request.POST["Injury_Illeness"]),
        except:
            i=False
        try:
            p=request.POST["property_damage"], 
        except:
            p=False
        try:
            v=request.POST["vehicle"],  
        except:
            v=False
        Incident.objects.create(
        location=request.POST["location"],
        description=request.POST["description"],
        date=request.POST["date"],   
        time=request.POST["time"],
        incident_Location=request.POST["incident_location"],
        severity=request.POST["severity"], 
        suspected_Cause=request.POST["cause"], 
        immediate_Action=request.POST["action"],
        environmental_Incident=bool(env),
        Injury_Illeness=bool(i),
        reported_by=request.POST["reported"],
        property_damage=bool(p),
        vehicle=bool(v),)
        if button=='save':
            return render(request, 'input.html')
        return redirect('/')
    else:
        return render(request, 'input.html')