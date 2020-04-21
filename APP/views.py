from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def in(request):
# 	return HttpResponse('你好，汪豪')

def test(request):
	return render(request, 'test_1.html')


def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)

from django.template import loader

from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/test.html', context)

from django.shortcuts import get_object_or_404, render

def details(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def temindex(request):
	return render(request, 'test/index.html')


