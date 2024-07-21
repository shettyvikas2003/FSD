from django.shortcuts import render

# Create your views here.
def showlist(request):
    fruits=["Apple","Mango","orange"]
    student_name=["Vikas","Varshitha","Yogitha","Sukesh"]
    return render(request, 'showlist.html',{"fruitsnew":fruits, "student_namenew":student_name})