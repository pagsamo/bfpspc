from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Barangay(models.Model):
    Name = models.CharField(max_length=255)
    Latitude = models.DecimalField(decimal_places=7, max_digits=20)
    Longitude = models.DecimalField(decimal_places=7, max_digits=20)

    def __str__(self):
        return self.Name


class InvestigatorRank(models.Model):
    Code = models.CharField(max_length=100)
    Definition = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.Code


class Investigator(models.Model):
    FirstName = models.CharField(max_length=100)
    MiddleName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Rank = models.ForeignKey(InvestigatorRank,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        delimeter = ' '
        FullName = [self.Rank, self.FirstName, self.MiddleName, self.LastName]
        FullNameMap = map(lambda i:i.__str__(), FullName)
        FullNameList = list(FullNameMap)
        return delimeter.join(FullNameList)

    class Meta:
        unique_together = (('FirstName', 'LastName'),)

class OccupancyType(models.Model):
    Description = models.CharField(max_length=100)

    def __str__(self):
        return self.Description


class Incident(models.Model):
    DateTime = models.DateTimeField()
    FireOutDateTime = models.DateTimeField(null=True, blank=True)
    HouseNumber = models.CharField(max_length=255,blank=True)
    Street = models.CharField(max_length=255,blank=True)
    Barangay = models.ForeignKey(Barangay, on_delete=models.SET_NULL, null=True)
    OccupancyType = models.ForeignKey(OccupancyType, on_delete=models.SET_NULL, null=True)
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
    FireArsonInvestigator = models.ForeignKey(Investigator, on_delete=models.SET_NULL, null=True)
    REMARKS_CHOICES = [
        ('closed', 'Closed'),
        ('under investigation', 'Under Investigation'),
    ]

    Remarks = models.CharField(max_length=255, choices=REMARKS_CHOICES, default='closed', blank=True)
    Notes = models.TextField(default="", blank=True)

    def __str__(self):
        delimeter = ' '
        FullName = [self.DateTime, self.OwnerEstablishmentName]
        FullNameMap = map(lambda i:i.__str__(), FullName)
        FullNameList = list(FullNameMap)
        return delimeter.join(FullNameList)
    
    


