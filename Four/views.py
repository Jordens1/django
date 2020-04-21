import hashlib
import random
from time import time

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def firf(request):
    reponse = HttpResponse()
    reponse.content = 'xishi万岁'
    reponse.status_code = 404
    return reponse


def sec(request):
    if  random.randrange(10) > 5:
        url = reverse('fou:firf')
        return HttpResponseRedirect(url)

    return HttpResponse('正常')



def set_cookie(request):
    reponse = HttpResponse('设置成功')
    reponse.set_cookie('username' ,'xishi')
    reponse.set_signed_cookie('username' ,'xishi')
    # request.COOKIES.get('username')
    return reponse


def get_cookie(request):
    Uname = request.COOKIES.get('uname')
    return HttpResponse(Uname)


def login(request):
    return render(request, 'cookieh/login.html')

def do_login(request):
    uname = request.COOKIES.get('uname')
    #uname = request.get_signed_cookie('content', salt='rock')

    if uname:
        return HttpResponseRedirect(reverse('fou:login'))
    else:
        reponse = HttpResponseRedirect(reverse('fou:get-cookie'))
        reponse.set_cookie('uname', uname)
        # return reponse

def jiami(request):
    uname = request.get_signed_cookie('content', salt='rock')
    if uname:
    # HttpResponseRedirect(reverse('fou:login'))
        return render(request, 'cookieh/login.html', locals())
    return redirect(reverse('fou:logout'))



def do_loginout(request):
    request = redirect(reverse('fou:mine'))
    # del request.session['username']
    # request.delete_cookie('username')
    request.flush()

    return request


def do_inout(request):
    if request.method == "GET":
        # return render(request, 'cookieh/login.html')
    # elif request.method == 'POST':
        username = request.COOKIES.get('username')
        request.session['username'] = username
        return HttpResponse('设置成功')


def mine(request):
    username = request.session.get('username')
    return render(request, 'cookieh/twomine.html', locals())

from .models import Student
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            s = Student()
            s.s_name = username
            s.s_pass = password
            s.save()
        except  Exception as e:
            return HttpResponse('lose')
    elif request.method == 'GET':
        request = render(request, 'cookieh/stu_regist.html')
        return request
    return HttpResponse('yes')

def stu_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        studw = Student.objects.filter(s_name=username).filter(s_pass=password)
        if studw.exists():
            student = studw.first()
            ip = request.META.get('REMOTE_ADDR')
            token1 = gen_token(ip)

        return HttpResponse(studw.s_name)
    elif request.method == 'GET':
        request = render(request, 'cookieh/stu_login.html')
        return request
    return HttpResponse('yes')



def gen_token(ip):
    c_time = time()
    r = random.random()
    return hashlib.new( 'md5', (str(ip) + str(c_time) + str(r)).encode() ).hexdigest()





