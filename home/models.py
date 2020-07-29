from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Barangay(models.Model):
    Name = models.CharField(max_length=255)
    Latitude = models.IntegerField(default=0)
    Longitude = models.IntegerField(default=0)

    def __str__(self):
        return self.Name


class InvestigatorRank(models.Model):
    Code = models.CharField(max_length=255)
    Definition = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.Code


class Investigator(models.Model):
    FirstName = models.CharField(max_length=255)
    MiddleName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Rank = models.ForeignKey(InvestigatorRank,on_delete=models.CASCADE)

    def __str__(self):
        delimeter = ' '
        FullName = [self.Rank, self.FirstName, self.MiddleName, self.LastName]
        FullNameMap = map(lambda i:i.__str__(), FullName)
        FullNameList = list(FullNameMap)
        return delimeter.join(FullNameList)

class Incident(models.Model):
    DateTime = models.DateTimeField()
    FireOutDateTime = models.DateTimeField(null=True, blank=True)
    HouseNumber = models.CharField(max_length=255,blank=True)
    Street = models.CharField(max_length=255,blank=True)
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
    Injuries = models.IntegerField(default=0)
    FatalitiesMale = models.IntegerField(default=0)
    FatalitiesFemale = models.IntegerField(default=0)
    TotalFatalities = models.IntegerField(default=0)
    EstimatedDamageCost = models.IntegerField(default=0)
    FinalDamageCost = models.IntegerField(default=0)
    Origin = models.CharField(max_length=255, blank=True)
    Cause = models.TextField(blank=True)
    FireArsonInvestigator = models.ForeignKey(Investigator, on_delete=models.CASCADE)
    REMARKS_CHOICES = [
        ('closed', 'Closed'),
        ('under investigation', 'Under Investigation')
    ]

    Remarks = models.CharField(max_length=255, choices=REMARKS_CHOICES, default='closed')
    Notes = models.TextField(default="", blank=True)

    def __str__(self):
        delimeter = ' '
        FullName = [self.DateTime, self.OwnerEstablishmentName]
        FullNameMap = map(lambda i:i.__str__(), FullName)
        FullNameList = list(FullNameMap)
        return delimeter.join(FullNameList)
    
    


