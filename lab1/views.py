
import datetime
from django.http import HttpResponse
from django.shortcuts import render

def current_date(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s</body></html>" %now
    return HttpResponse(html)
def current_date_aftersix(request):
    dt = datetime.datetime.now() + datetime.timedelta(hours=6)
    html = "<html><body>It is after %s</body></html>" %(dt,)
    return HttpResponse(html)
def current_date_beforesix(request):
    dtb = datetime.datetime.now() + datetime.timedelta(hours=-6)
    html = "<html><body>It is before %s</body></html>" %(dtb,)
    return HttpResponse(html)