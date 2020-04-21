from django.db.models import Avg, F, Q
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def two(request):
	return render(request, 'test/index.html')

from .models import Student

def add(request):
	student = Student()
	student.s_name = 'xiaohong'
	student.s_age = 23
	student.save()
	return HttpResponse('is ok')

def get(request):
	studentInfo = Student.objects.all()
	# studentInfo = Student.objects.get(pk=1)
	students = {'studentInfo': studentInfo}
	return render(request, 'stud/get_stud.html', students)

from .models import Person
import random
def add_persons(request):
	list = []
	for i in range(10):
		person = Person()
		flag = random.randrange(100)
		if flag not in list:
			list.append( flag )
			person.p_name = 'Tom%d' %flag
			person.p_age = i
			person.p_sex = i % 2
			person.save()
	return HttpResponse('创建完成')

def get_person(request):
	# c= Person.objects.all()[2:5]   左闭右开
	# c= Person.objects.filter(p_age__gt=4).order_by('p_age')
	# c1= Person.objects.filter(p_age__in=[4, 8]).order_by('-p_age').first()
	c1= Person.objects.filter(p_age__in=[4, 8]).order_by('-p_age')  #改成负数，就是降序
	c3 = Person.objects.aggregate(Avg('g_age'))
	c4 = Person.objects.filter(p_age__gt=F('p_name')-10)
	c5 = Person.objects.filter(Q(p_age__gt=2) & Q(p_age__lt=5))
	print(c1.count())
	if c1.exists():
		print(c1.first())
	else:
		print('not')
	context = {
		'person': c1
	}
	return render(request, 'people/getpeo.html', context=context)
	# return HttpResponse(c.p_age)

from .models import Animal
def get_animal(request):
	c = Animal.objects.all()
	context = {
		'an': c
	}
	return render(request, 'anminal/an.html', context=context)