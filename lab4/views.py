from django.shortcuts import render

# Create your views here.
def tableshow(request):
    s1={"sname":"Vikas","scode":"21CS62"}
    s2={"sname":"Shreyas","scode":"21CS63"}
    s3={"sname":"Sujan","scode":"21CS61"}
    s4={"sname":"Sathwik","scode":"21CS64"}
    l=list()
    l=[s1,s2,s3,s4]
    return render(request, 'vikastable.html',{"l":l})