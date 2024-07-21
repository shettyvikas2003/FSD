from crypt import methods
import csv
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from studentform.models import course, projectreg, student

# Create your views here.
def insert(request):
    s1 = student(student_name = 'Shreyas', student_usn = '4vp21cs096', student_sem = 6)
    s2 = student(student_name = 'Shodhan', student_usn = '4vp21cs090', student_sem = 6)     
    s3 = student(student_name = 'Sujan', student_usn = '4vp21cs100', student_sem = 6)
    c1 = course(course_name = 'Full Stack', course_code = '21cs62', course_credit = 4)
    c2 = course(course_name = 'Software', course_code = '21cs61', course_credit = 3)     
    c3 = course(course_name = 'Data Science', course_code = '21cs63', course_credit = 1)
    
    s1.save()
    s2.save()   
    s3.save()
    c1.save()
    c2.save()
    c3.save()
    
    return HttpResponse('Success!!!!!')

def retrive_data(request):
        students = student.objects.all()
        courses = course.objects.all()
        return render(request, 'form.html', {'students': students, 'courses': courses})



def req(request):
    if request.method == 'POST':
        sid = request.POST.get("sname")
        cid = request.POST.get("cname")
        students = student.objects.get(id = sid)
        courses = course.objects.get(id = cid)
        res = students.enrollment.filter(id=cid)
        
        if res: 
            return HttpResponse('Student Already Enrolled !!')
        
        students.enrollment.add(courses)
        return HttpResponse('Student Enrolled Sucessfully !!')
    else:
        students = student.objects.all()
        courses = course.objects.all()
        return render(request, 'form.html', {'students': students, 'courses': courses})


def display(request):
    if request.method == 'POST':
        cid = request.POST.get("cname")
        courses = course.objects.get(id = cid)
        students = student.objects.all()
        cos = course.objects.all()
        student_list = []
        
        for stud in students:
            if stud.enrollment.filter(id = cid):
                student_list.append(stud)
        
        return render(request, 'display.html', {'students': student_list, 'courses': cos})
    else:
        courses = course.objects.all()
        return render(request, 'display.html', {'courses': courses})

    
class studentlistview(generic.ListView):
    model = student
    template_name = 'student_list.html'
    
class detailedview(generic.DetailView):
        model = student
        template_name = 'student_detailed_list.html'



def createcsv(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename = "course_data.csv"'
    writer = csv.writer(response)
    s = student.objects.all()
    writer.writerow(['Name','USN','Sem'])
    for stud in s:
        writer.writerow([stud.student_name, stud.student_usn, stud.student_sem])
        
    return response


def createpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename = "student_data.pdf"'
    w = canvas.Canvas(response)
    s = student.objects.all()
    y = 600
    w.drawString(70,y,'Student name')
    w.drawString(170,y,'Student usn')
    w.drawString(270,y,'Student sem')
    y = 540
    for stud in s:
        w.drawString(70,y,stud.student_name)
        w.drawString(170,y,stud.student_usn)
        w.drawString(270,y,str(stud.student_sem))
        y = y - 60
        
    w.showPage()
    w.save()
    return response


    
def addproject(request):
    if request.method == 'POST':
        form = projectreg(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success !!")
        else:
            return HttpResponse("Failed !!")
    else:
        form = projectreg()
        return render(request, 'projectreg.html', {'form':form})
        
    
        
def reqwithajax(request):
    if request.method == 'POST':
        sid = request.POST.get("sname")
        cid = request.POST.get("cname")
        students = student.objects.get(id = sid)
        courses = course.objects.get(id = cid)
        res = students.enrollment.filter(id=cid)
        
        if res: 
            return HttpResponse('Student Already Enrolled !!')
        
        students.enrollment.add(courses)
        return HttpResponse('Student Enrolled Sucessfully !!')
    else:
        students = student.objects.all()
        courses = course.objects.all()
        return render(request, 'ajax.html', {'students': students, 'courses': courses})

    
    
def ajaxdisplay(request):
    if request.method == 'POST':
        cid = request.POST.get("cname")
        courses = course.objects.get(id = cid)
        students = student.objects.all()
        cos = course.objects.all()
        student_list = []
        
        for stud in students:
            if stud.enrollment.filter(id = cid):
                student_list.append(stud)
        
        return render(request, 'selectedcourse.html', {'students': student_list, 'courses': cos})
    else:
        courses = course.objects.all()
        return render(request, 'selectedcourse.html', {'courses': courses})