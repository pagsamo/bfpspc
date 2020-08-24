from home.models import Incident

incidents = Incident.objects.all()
earliest = Incident.objects.earliest('DateTime')
latest = Incident.objects.latest('DateTime')

def month(i):
    switcher = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec',
    }
    return switcher.get(i, "Invalid Month")

def overTime():
    overTime = {}
    for x in range(earliest.DateTime.year, (latest.DateTime.year+1)):
        if x == earliest.DateTime.year:
            for y in range(earliest.DateTime.month, 13):
                overTime.update({"%s %s" %(month(y), x): incidents.filter(DateTime__year=x, DateTime__month=y).count()})
        elif x == latest.DateTime.year:
            for y in range(1, (latest.DateTime.month+1)):
                overTime.update({"%s %s" %(month(y), x): incidents.filter(DateTime__year=x, DateTime__month=y).count()})
        else:
            for y in range(1, 13):
                overTime.update({"%s %s" %(month(y), x): incidents.filter(DateTime__year=x, DateTime__month=y).count()})