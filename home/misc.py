from home.models import Incident

incidents = Incident.objects.all()
earliest = Incident.objects.earliest('DateCalled')
latest = Incident.objects.latest('DateCalled')

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
    for x in range(earliest.DateCalled.year, (latest.DateCalled.year+1)):
        if x == earliest.DateCalled.year:
            for y in range(earliest.DateCalled.month, 13):
                overTime.update({"%s %s" %(month(y), x): incidents.filter(DateCalled__year=x, DateCalled__month=y).count()})
        elif x == latest.DateCalled.year:
            for y in range(1, (latest.DateCalled.month+1)):
                overTime.update({"%s %s" %(month(y), x): incidents.filter(DateCalled__year=x, DateCalled__month=y).count()})
        else:
            for y in range(1, 13):
                overTime.update({"%s %s" %(month(y), x): incidents.filter(DateCalled__year=x, DateCalled__month=y).count()})