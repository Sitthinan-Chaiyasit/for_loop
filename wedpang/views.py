from django.shortcuts import render
from . import models

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def for_view(request):
    context = {}
    context['message'] = "การวนซ้ำใน_Django"
    
    if request.method == 'POST' and request.POST.get('count') != '':
        number = int(request.POST.get('count'))
        context['count'] = list(range(1,number +1))
    else:
        context['count'] = list(range(1, 2))
        
    return render(request, 'for.html',context)

def multipli(request):
    context = {}
    context['message'] = "ตารางสูตรคูณ"
    
    number = 1
    if request.method == 'POST' and request.POST.get('number') != '':
        try:
            number = int(request.POST.get('number'))
        except ValueError:
            number = 1
    context['number'] = number
    context['table'] = [(i, number * i) for i in range(1, 13)]
        
    return render(request, 'multiplication.html', context)

def students(request):
    context = {}
    context['title'] = "รายชื่อนักเรียน"
    students = models.Students.objects.all()
    context['students'] = students
    return render(request, 'students.html', context)