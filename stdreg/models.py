from django.db import models
from django.forms import ModelForm

# Create your models here.
class Course(models.Model):
    course_code=models.CharField(max_length=30)
    course_name=models.CharField(max_length=30)
    course_credit=models.IntegerField()
    def __str__(self):
        return self.course_name
class Student(models.Model):
    student_usn=models.CharField(max_length=30)
    student_name=models.CharField(max_length=30)
    student_sem=models.IntegerField()
    enrolment=models.ManyToManyField(Course)
    def __str__(self):
        return self.student_name+"("+self.student_usn+")"
class Project(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    ptopic=models.CharField(max_length=300)
    planguage=models.CharField(max_length=100)
    pduration=models.IntegerField()
    
class ProjectReg(ModelForm):
        required_css_class="required"
        class Meta:
            model=Project
            fields=['student','ptopic','planguage','pduration']