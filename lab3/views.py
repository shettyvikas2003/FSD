from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def createtable(request,s,n):
    result=""
    for i in range(1,n+1):
        result+="<p>"+str(s)+"*"+str(i)+"="+str((s*i))+"</p>"
    return HttpResponse(result)