from django.shortcuts import render

# Create your views here.
from django.db.models import Avg, F, Q
from django.http import HttpResponse
from django.template import loader


def index(request):
    '''
    本质上就是返回的HTTPresponse，帮我们把context数据渲染成了模板
    temp = loader.get_template('in/in.html')
    content = temp.render()
    return HttpResponse(content)
    '''
    conetxt = {}
    # return render(request, 'in/in.html', context=conetxt)
    return HttpResponse('nihao')

from .models import Stud
def getInfo(reuqest):
    # stualll = Stud.objects.all().filter(s_name='33')
    stualll = Stud.objects.all()
    stu_dir = {'class': 'a1', 'zuowei': '33', }
    data = {
        'stuall': stualll,
        'stu_dir': stu_dir,
        'count': 90,
    }
    return render(reuqest, 'in/info.html', data)


def jicheng(request):
    Title = 'base'
    return render(request, 'in/home.html', context=locals())


def have_request(request):
    # ?hobby=x   request.GET.get('hobby')  request.GET.getlist('hobby')  一个key对应的多个值，是一个类似字典的东西
    # context = { 'path' : request.path,
    #             'method': request.method,
    #             'get': request.GET,
    #             'post': request.POST,
    # }
    print(request.path)
    return render(request, 'in/requ.html', context={})







