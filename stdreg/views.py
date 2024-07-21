import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from stdreg.models import Course, ProjectReg, Student
from reportlab.pdfgen import canvas
# Create your views here.
def insert(request):
    m=Student(student_name='Vikas',student_usn='4VP01',student_sem=6)
    m.save()
    m=Student(student_name='Yogitha',student_usn='4VP02',student_sem=5)
    m.save()
    m=Student(student_name='Varshitha',student_usn='4VP03',student_sem=6)
    m.save()
    m=Student(student_name='Yashwitha',student_usn='4VP04',student_sem=7)
    m.save()
    m=Course(course_code='21CS01',course_name='SE',course_credit=6)
    m.save()
    m=Course(course_code='21CS02',course_name='FSD',course_credit=8)
    m.save()
    m=Course(course_code='21CS03',course_name='CGIP',course_credit=5)
    m.save()
    m=Course(course_code='21CS04',course_name='ME',course_credit=5)
    m.save()
    return HttpResponse("Data Inserted Successfully")
    
def reg(request):
    if request.method=="POST":
        sid=request.POST.get("sname")
        cid=request.POST.get("cname")
        s=Student.objects.get(id=sid)
        c=Course.objects.get(id=cid)
        res=s.enrolment.filter(id=cid)
        if res:
            return HttpResponse("Student already enrolled for course")
        s.enrolment.add(c)
        return HttpResponse("Student enrolled into course")
    else:
        student=Student.objects.all()
        course=Course.objects.all()
    return render(request,'register.html',{"students": student,"courses":course})

def display(request):
    if request.method=="POST":
        cid=request.POST.get("cname")
        s=Student.objects.all()
        student_list=list()
        for student in s:
            if student.enrolment.filter(id=cid):
                student_list.append(student)
        if len(student_list)==0:
            return  HttpResponse("No students enrolled")
        
        return render(request,'stdlist.html',{"student_list":student_list})
    else:
        course=Course.objects.all()
    return render(request,'select.html',{"courses":course})
def reg_project(request):
    if request.method=="POST":
      form=ProjectReg(request.POST)  
      if form.is_valid():
          form.save()
          return HttpResponse("Project registered successfully ")
      else:
          return HttpResponse("Project registration failed")
    else:    
        form= ProjectReg()
        return render(request,'projreg.html',{'form':form})
class StudentListView(generic.ListView):
    model=Student
    template_name='student_list.html'
class StudentDetailView(generic.DetailView):
    model=Student
    template_name='student_details.html'
def create_csv(request):
    response=HttpResponse(content_type="text/csv")
    response['Content-Disposition']='attachment; filename="course_data.csv"'
    courses=Course.objects.all()
    writer=csv.writer(response)
    writer.writerow(['CourseName','CourseCode','CourseCredit'])
    for course in courses:
        writer.writerow([course.course_name,course.course_code,course.course_credit])
    return response
def create_pdf(request):
    response=HttpResponse(content_type="application/pdf")
    response['Content-Disposition']='attachment; filename="course_datapdf.pdf"'
    courses=Course.objects.all()
    c=canvas.Canvas(response)
    y=600
    for course in courses:
        c.drawString(70,y,course.course_name)
        c.drawString(170,y,course.course_code)
        c.drawString(270,y,str(course.course_credit))
        y=y-60
    c.showPage()
    c.save()
    return response
    
