from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Barangay(models.Model):
    Name = models.CharField(max_length=255)


class InvestigatorRank(models.Model):
    Code = models.CharField(max_length=255)
    Definition = models.CharField(max_length=255)


class Investigator(models.Model):
    FirstName = models.CharField(max_length=255)
    MiddleName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Rank = models.ForeignKey(InvestigatorRank,on_delete=models.CASCADE)


class Incident(models.Model):
    DateTime = models.DateTimeField()
    FireOutDateTime = models.DateTimeField()
    HouseNumber = models.CharField(max_length=255)
    Street = models.CharField(max_length=255)
    OCCUPANCY_CHOICES = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
    ]
    Barangay = models.ForeignKey(Barangay, on_delete=models.CASCADE)
    OccupancyType = models.CharField(max_length=255, choices=OCCUPANCY_CHOICES, default='residential')
    OwnerEstablishmentName = models.CharField(max_length=255)
    ALARM_LEVEL_CHOICES = [
        ('1','1'),
        ('2', '2'),
        ('3', '3'),
    ]
    AlarmLevel = models.CharField(max_length=1, choices=ALARM_LEVEL_CHOICES, default='1')
    Injuries = models.IntegerField()
    FatalitiesMale = models.IntegerField()
    FatalitiesFemale = models.IntegerField()
    TotalFatalities = models.IntegerField()
    EstimatedDamageCost = models.IntegerField()
    FinalDamageCost = models.IntegerField()
    Origin = models.CharField(max_length=255)
    Cause = models.TextField()
    FireArsonInvestigator = models.ForeignKey(Investigator, on_delete=models.CASCADE)
    REMARKS_CHOICES = [
        ('closed', 'Closed'),
        ('under investigation', 'Under Investigation')
    ]

    Remarks = models.CharField(max_length=255, choices=REMARKS_CHOICES, default='closed')
    Notes = models.TextField()
    
    @property
    def save(self):
        self.TotalFatalities = self.FatalitiesFemale + self.FatalitiesMale
        return super(Incident, self).save()
    


