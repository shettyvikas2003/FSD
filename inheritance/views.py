from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'Home.html')

def Aboutus(request):
    return render(request,'Aboutus.html')

def Contact(request):
    return render(request,'Contact.html')
    
    