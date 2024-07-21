"""
URL configuration for FSD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path


from cookie.views import cookiedemo, expr
from databasecourse.views import delete_demo, insert_demo, retreive_demo, retrieve, update_demo
from inheritance.views import Aboutus, Contact, Home

from inhertance1.views import contact1, home1
from lab3.views import createtable
from lab2.views import showlist
from lab1.views import current_date, current_date_aftersix, current_date_beforesix
from lab4.views import tableshow
from stdreg.views import StudentDetailView, StudentListView, create_csv, create_pdf, display, insert, reg, reg_project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cdt/',current_date),
    path('cdta/',current_date_aftersix),
    path('cdtb/',current_date_beforesix),
    path('showlist/',showlist),
    path('cts/<int:s>/<int:n>/',createtable),
    path('vikastable/',tableshow),
    path('home/',Home),
    path('aboutus/',Aboutus),
    path('contact/',Contact),
    path('home1/',home1),
    path('contact1/',contact1),
    path('insert/',insert_demo),
    path('update/',update_demo),
    path('delete/',delete_demo),
    path('retreive/',retreive_demo),
    path('retreivenew/<str:s>/',retrieve),
    path('insertstd/',insert),
    path('regs/',reg),
    path('displaystd/',display),
    path('reg_proj/',reg_project),
    path('stdlist/',StudentListView.as_view()),
    path('csv_path/',create_csv),
    path('csv_pdf/',create_pdf),
    path('stddetail/<int:pk>/',StudentDetailView.as_view()),
    path('cookiedemo/',cookiedemo), 
    path('expr/',expr),
]
