from django.http import HttpResponse
from django.shortcuts import render

from databasecourse.models import meeting

# Create your views here
def insert_demo(request):
    m=meeting(meeting_code='m002',meeting_dt="2024-04-10",meeting_subject="WTW",meeting_np="50")
    m.save()
    m=meeting(meeting_code='m003',meeting_dt="2024-04-11",meeting_subject="parents",meeting_np="60")
    m.save()
    m=meeting(meeting_code='m004',meeting_dt="2024-04-10",meeting_subject="ABC",meeting_np="50")
    m.save()
    m=meeting(meeting_code='m005',meeting_dt="2024-04-10",meeting_subject="DEF",meeting_np="50")
    m.save()
    return HttpResponse("Record created successfully")
from django.db.models import Q
def update_demo(request):
    m=meeting.objects.get(meeting_code="m005")
    m.meeting_dt="2024-04-10"
    m.meeting_np=50
    m.save()
    return HttpResponse("<h1>Record updated successfully</h1>")

def delete_demo(request):
    m=meeting.objects.get(meeting_code="m003")
    m.delete()
    return HttpResponse("<h1>Record deleted successfully</h1>")

def retreive_demo(request):
    m=meeting.objects.filter(Q(meeting_subject__contains="ABC") & Q(meeting_np__lte="50"))
    result=""
    for Meeting in m:
        result+="<p>%s,%s,%s,%s</p>"%(Meeting.meeting_code, Meeting.meeting_subject,Meeting.meeting_dt,Meeting.meeting_np)
    return HttpResponse(result)

def retrieve(request,s):
    result=""
    if(str(s)=='like'):
       obj=meeting.objects.filter(meeting_code__contains="m002")
    elif(str(s)=='all'):
       obj=meeting.objects.all()
    elif(str(s)=='get'):
       obj=meeting.objects.get(meeting_code__contains="m004")
       result+="<tr><td>%s</td><td>%s</td><td>%s</td></tr>"%(obj.meeting_code,obj.meeting_subject,obj.meeting_dt)
       return HttpResponse("<table border>"+result+"</table>")
    elif(str(s)=='slice'):
      obj=meeting.objects.all()[:1]
    for meet in obj:
      result+="<tr><td>%s</td><td>%s</td><td>%s</td></tr>"%(meet.meeting_code,meet.meeting_subject,meet.meeting_dt)
    return HttpResponse("<table border>"+result+"</table>")