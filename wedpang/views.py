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
    context['message'] = "การวนซ้ำใน Django"
    number = request.POST.get('count')
    if request.method == 'POST' and number:
        try:
            number = int(number)
            context['count'] = list(range(1, number + 1))
        except ValueError:
            context['count'] = []
    else:
        context['count'] = []
    return render(request, 'for.html', context)

def multipli(request):
    context = {}
    context['message'] = "ตารางสูตรคูณ"
    number = request.POST.get('number')
    try:
        number = int(number) if number else 1
    except ValueError:
        number = 1
    context['number'] = number
    context['table'] = [(i, number * i) for i in range(1, 13)]
    return render(request, 'multiplication.html', context)

def students(request):
    context = {}
    context['title'] = "รายชื่อนักเรียน"
    if request.method == 'POST':
        stuid = request.POST.get('stuid')
        name_prefix = request.POST.get('name_prefix')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        if stuid and name_prefix and first_name and last_name and age:
            models.Students.objects.create(
                stuid=stuid,
                name_prefix=name_prefix,
                first_name=first_name,
                last_name=last_name,
                age=age
            )
            return redirect('students')
    students = models.Students.objects.all()
    context['students'] = students
    return render(request, 'students.html', context)