from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
import datetime

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Designation = models.CharField(max_length=100)


class Barangay(models.Model):
    Name = models.CharField(max_length=75)
    geom = models.MultiPolygonField(srid=4326, null=True, blank=True)

    def IncidentCount(self):
        return self.incident_set.count()

    def IncidentInstances(self):
        return self.incident_set.all()

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ('Name',)


class Rank(models.Model):
    Code = models.CharField(max_length=100, unique=True)
    Definition = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.Code

#####################
#Personnel
#####################
class Personnel(models.Model):
    FirstName = models.CharField(max_length=100, blank=True, null=True)
    MiddleName = models.CharField(max_length=100, blank=True, null=True)
    LastName = models.CharField(max_length=100)
    Rank = models.ForeignKey(Rank,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        delimeter = ' '
        FullName = [self.Rank, self.FirstName, self.MiddleName, self.LastName]
        FullNameMap = map(lambda i:i.__str__(), FullName)
        FullNameList = list(FullNameMap)
        return delimeter.join(FullNameList)

    class Meta:
        unique_together = (('FirstName', 'LastName'),)
#####################
#Personnel
#####################

#####################
#Engines
#####################
class Engines(models.Model):
    Name = models.CharField(max_length=255,blank=True, null=True)
    Model = models.CharField(max_length=255,blank=True, null=True)
    Remarks = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.Name
 #####################
#Engines
#####################   

#####################
#Incident
#####################
class Incident(models.Model):
    ##phase 1
    DateAlarmReceived = models.DateField(blank=True, null=True)
    TimeAlarmReceived = models.TimeField(blank=True, null=True)
    Caller = models.CharField(max_length=255,blank=True, null=True)
    CallerAddress = models.CharField(max_length=255,blank=True, null=True)
    PersonnelReceivingCall = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True, blank=True)
    HouseNumber = models.CharField(max_length=255,blank=True, null=True)
    Street = models.CharField(max_length=255,blank=True, null=True)
    Barangay = models.ForeignKey(Barangay, on_delete=models.SET_NULL, null=True, blank=True)
    Location = models.PointField(blank=True, null=True)
    ##phase 2 - incident response -> see new model
    ##phase 3 - AlarmStatus
    ##phase 4 
    OCCUPANCYTYPE_CHOICES = [
        ('Structural/Residential', 'Structural/Residential'),
        ('Non Structural', 'Non Structural'),
        ('Vehicular','Vehicular'),
    ]
    OccupancyType = models.CharField(max_length=255, choices=OCCUPANCYTYPE_CHOICES, blank=True, null=True)
    OccupancyTypeRemarks = models.CharField(max_length=255, blank=True, null=True)
    DistanceFromBase = models.IntegerField(default=0)
    DescriptionOfStructure = models.TextField(blank=True, null=True)
    #7 casualty
    InjuredCivilianM = models.IntegerField(default=0)
    InjuredCivilianF = models.IntegerField(default=0)
    InjuredFireFighterM = models.IntegerField(default=0)
    InjuredFireFighterF = models.IntegerField(default=0)
    DeathCivilianM = models.IntegerField(default=0)
    DeathCivilianF = models.IntegerField(default=0)
    DeathFireFighterM = models.IntegerField(default=0)
    DeathFireFighterF = models.IntegerField(default=0)
    #Breathing apparatus
    #15 Details Narrative
    Details = models.TextField(blank=True, null=True)
    Problems = models.TextField(blank=True, null=True)
    Observations = models.TextField(blank=True, null=True)
    OwnerName = models.CharField(max_length=255, blank=True, null=True)
    Occupant = models.CharField(max_length=255, blank=True, null=True)
    EstablishmentName = models.CharField(max_length=255, blank=True, null=True)
    EstimatedDamageCost = models.IntegerField(default=0)
    #Can be the final phase
    FinalDamageCost = models.IntegerField(default=0)
    Origin = models.CharField(max_length=255, blank=True, null=True)
    Cause = models.TextField(blank=True, null=True)
    #alarm status
    DateTimeUnderControl = models.DateTimeField(blank=True, null=True)
    DateTimeFireOut = models.DateTimeField(blank=True, null=True)
    Time1stAlarm = models.TimeField(blank=True, null=True)
    GCommander1stAlarm = models.CharField(max_length=255, blank=True)
    Time2ndAlarm = models.TimeField(blank=True, null=True)
    GCommander2ndAlarm = models.CharField(max_length=255, blank=True)
    Time3rdAlarm = models.TimeField(blank=True, null=True)
    GCommander3rdAlarm = models.CharField(max_length=255, blank=True)
    Time4thAlarm = models.TimeField(blank=True, null=True)
    GCommander4thAlarm = models.CharField(max_length=255, blank=True)
    Time5thAlarm = models.TimeField(blank=True, null=True)
    GCommander5thAlarm = models.CharField(max_length=255, blank=True)
    TimeAlphaAlarm = models.TimeField(blank=True, null=True)
    GCommanderAlphaAlarm = models.CharField(max_length=255, blank=True)
    TimeBravoAlarm = models.TimeField(blank=True, null=True)
    GCommanderBravoAlarm = models.CharField(max_length=255, blank=True)
    TimeCharlieAlarm = models.TimeField(blank=True, null=True)
    GCommanderCharlieAlarm = models.CharField(max_length=255, blank=True)
    TimeDeltaAlarm = models.TimeField(blank=True, null=True)
    GCommanderDeltaAlarm = models.CharField(max_length=255, blank=True)
    TimeEchoAlarm = models.TimeField(blank=True, null=True)
    GCommanderEchoAlarm = models.CharField(max_length=255, blank=True)
    TimeHotelAlarm = models.TimeField(blank=True, null=True)
    GCommanderHotelAlarm = models.CharField(max_length=255, blank=True)
    TimeIndiaAlarm = models.TimeField(blank=True, null=True)
    GCommanderIndiaAlarm = models.CharField(max_length=255, blank=True)
    TimeGeneralAlarm = models.TimeField(blank=True, null=True)
    GCommanderGeneralAlarm = models.CharField(max_length=255, blank=True)
    REMARKS_CHOICES = [
        ('closed', 'Closed'),
        ('under investigation', 'Under Investigation'),
        ('',''),
    ]
    Remarks = models.CharField(max_length=255, choices=REMARKS_CHOICES, default='closed', blank=True)
    Approved = models.BooleanField(default=False)

    def __str__(self):
        delimeter = ' '
        FullName = [self.DateAlarmReceived, self.OwnerName]
        FullNameMap = map(lambda i:i.__str__(), FullName)
        FullNameList = list(FullNameMap)
        return delimeter.join(FullNameList)
    
    class Meta:
        unique_together = (('DateAlarmReceived', 'OwnerName',),)
        ordering = ('-DateAlarmReceived','Barangay',)
#####################
#Incident
#####################


#####################
#AlarmStatusUponArrival
#####################
class AlarmStatusUponArrival(models.Model):
    Incident = models.ForeignKey(Incident, on_delete=models.SET_NULL, null=True, blank=True)
    STATUS_CHOICES = [
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd','3rd'),
    ]
    StatusUponArrival = models.CharField(max_length=255, choices=STATUS_CHOICES, default='', blank=True)
    StatusUponArrivalRemarks = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.StatusUponArrivalRemarks

    class Meta:
        unique_together = (('Incident', 'StatusUponArrival',),)
#####################
#AlarmStatusUponArrival
#####################


#####################
#IncidentResponse
#####################
class IncidentResponse(models.Model):
    Incident = models.ForeignKey(Incident, on_delete=models.SET_NULL, null=True, blank=True)
    Engine = models.ForeignKey(Engines, on_delete=models.SET_NULL, null=True, blank=True)
    TimeDispatched = models.TimeField(blank=True, null=True)
    TimeArrived = models.TimeField(blank=True, null=True)
    TimeReturnedToBase = models.TimeField(blank=True, null=True)
    WaterTankRefilled = models.IntegerField(default=0)
    GasConsumed = models.IntegerField(default=0)

    def ResponseTime(self):
        time1 = self.TimeDispatched.strftime("%H:%M")
        time2 = self.TimeArrived.strftime("%H:%M")
        ctime1 = datetime.datetime.strptime(time1, "%H:%M")
        ctime2 = datetime.datetime.strptime(time2, "%H:%M")
        difference = ctime2 - ctime1
        responseMins = difference.total_seconds() / 60
        return str(responseMins)
    

    def __str__(self):
        return self.TimeDispatched
#####################
#IncidentResponse
#####################

#####################
#BreathingApparatus
#####################
class BreathingApparatus(models.Model):
    Incident = models.ForeignKey(Incident, on_delete=models.SET_NULL, null=True, blank=True)
    BreathingApparatusNr = models.IntegerField(default=0)
    BreathingApparatusType = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.BreathingApparatusType

class ExtinguisingAgent(models.Model):
    Incident = models.ForeignKey(Incident, on_delete=models.SET_NULL, null=True, blank=True)
    Quantity = models.IntegerField(default=0)
    Type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.Incident
#####################
#BreathingApparatus
#####################


#####################
#RopeAndLadder
#####################
class RopeAndLadder(models.Model):
    Incident = models.ForeignKey(Incident, on_delete=models.SET_NULL, null=True, blank=True)
    Type = models.CharField(max_length=255, blank=True)
    Length = models.IntegerField(default=0)

    def __str__(self):
        return self.Incident
#####################
#RopeAndLadder
#####################

#####################
#HoseLine
#####################
class HoseLine(models.Model):
    Incident = models.ForeignKey(Incident, on_delete=models.SET_NULL, null=True, blank=True)
    Nr = models.IntegerField(default=0)
    Type = models.CharField(max_length=255, blank=True)
    Length = models.IntegerField(default=0)

    def __str__(self):
        return self.Incident
#####################
#HoseLine
#####################


#####################
#DutyPersonnel
#####################
class DutyPersonnel(models.Model):
    Incident = models.ForeignKey(Incident, on_delete=models.SET_NULL, null=True, blank=True)
    Personnel = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True, blank=True)
    Designation = models.CharField(max_length=255, blank=True)
    Remarks = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.Incident
#####################
#DutyPersonnel
#####################

# class SpotInvestigation(models.Model):
#     Incident = models.ForeignKey(Incident, on_delete=models.SET_NULL, null=True, blank=True)
#     ReportFor = models.CharField(max_length=255, blank=True)
#     ReportDate = models.DateField(blank=True, null=True)
#     Details = models.TextField(blank=True, null=True)
#     Disposition = models.TextField(blank=True, null=True)
#     PreparedBy = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True, blank=True,related_name = 'spot_prepared')
#     NoteBy = models.ForeignKey(Personnel, on_delete=models.SET_NULL, null=True, blank=True,related_name = 'spot_noted')

#####################
#Station
#####################
class Station(models.Model):
    Address = models.CharField(max_length=255, blank=True)
    TelephoneNumber = models.CharField(max_length=255, blank=True)
    PhoneNumbers = models.CharField(max_length=255, blank=True)
    EmailAddress = models.EmailField(blank=True, null=True)
    BFPLogo = ImageField(null=True)
    StationLogo = ImageField(null=True)
    ChiefOfficer = models.ForeignKey(Personnel,on_delete=models.SET_NULL, null=True, blank=True,related_name = 'officer_bfp')


    def __str__(self):
        return self.Address
#####################
#Station
#####################