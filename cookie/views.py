from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def cookiedemo(request):
    if "visit" in request.COOKIES:
        cnt=int(request.COOKIES["visit"])
        cnt += 1
        response=HttpResponse("<h1>You have visited %d times </h1>"%cnt)
        response.set_cookie("visit",cnt,max_age=2*24*60*60)
    else:
        cnt=1
        response=HttpResponse("<h1> You are visiting first time</h1>")
        response.set_cookie("visit",cnt,max_age=2*24*60*60)
    return response
def expr(request):
    return render(request,"expr.html")