from django.db import models

# Create your models here.
class Incident(models.Model):
    location =models.CharField(max_length=50)
    description =models.TextField()
    date =models.DateField(auto_now=False, auto_now_add=False)
    time =models.TimeField( auto_now=False, auto_now_add=False)
    incident_Location = models.TextField()
    severity = models.CharField(max_length=20)
    suspected_Cause = models.TextField()
    immediate_Action = models.TextField()
    reported_by = models.CharField(max_length=50)
    environmental_Incident = models.BooleanField(default=False)
    Injury_Illeness = models.BooleanField(default=False)
    property_damage = models.BooleanField(default=False)
    vehicle = models.BooleanField(default=False)
          
    