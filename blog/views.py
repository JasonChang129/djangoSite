from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
import datetime
from blog import models
# from blog.models import Book
from blog.models import Publish
from blog.models import Book


# Create your views here.
def template_language(req):
    names = ['lisi','zhangsan']
    return render(req,'template_index.html',{'list':names})

def current_time(reqest):
    # return HttpResponse('<h1>OK</h1>')
    date_time = datetime.datetime.now()
    return render(reqest,'render_one.html',{'now_time':date_time})

def userinfo(reqest):
    if reqest.method == 'POST':
        username = reqest.POST.get('username',None)
        gender = reqest.POST.get('gender',None)
        mail = reqest.POST.get('mail',None)
        age = reqest.POST.get('age',None)
        models.UserInfo.objects.create(
            user_name = username,
            gender = gender,
            mail = mail,
            age = age,
        )
    user_list = models.UserInfo.objects.all()
    return render(reqest,'userinfo.html',{'userList':user_list})

def year_2003_12(reqest,name):
    print('======================')
    return HttpResponse('zhangjainzhegn'+name)

def current_year(reqest,year,month):
    print('======================')
    return HttpResponse('当前时间：'+year+month)

def index(req):
    if req.method == 'POST':
        if 1:
            return redirect('/home/')
    return render(req,'login.html',{'num':3})

def login(req):
    p = '小王'
    return render(req,'home.html',{'name':p})

def ordered(req):
    return render(req,'ordered.html')

def shopping_car(req):
    return render(req,'shopping_car.html')

def data_oper(req):
    # obj = Publish.objects.filter(id=1)
    # print(obj[0].name)

    #基于对象的正向查询从book中查询出版商的city
    # publisher = models.Book.objects.filter(title='Go')[0].publisher
    # print(publisher.city)

    #基于对象的反向查询，从出版商中查询书籍
    obj = models.Publish.objects.filter(name='中信出版社')[0]
    print(obj.book_set.all().values('title').distinct())

    return HttpResponse('OK')