from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
import datetime
from blog import models
from blog.models import Publish
from blog.models import Book
from django.db.models import Avg,Min,Sum,Max
from django.db.models import F,Q


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
    # obj = models.Publish.objects.filter(name='中信出版社')[0]
    # print(obj.book_set.all().values('title').distinct())

    #双下划线的用法(__)
    #单表查询
    # obj = models.Book.objects.filter(id__gt=0).values('title')
    # obj = models.Book.objects.filter(id__lt=2).values('title')
    # obj = models.Book.objects.filter(id__in=[1,3]).values('title')
    # obj = models.Book.objects.filter(title__icontains='g').values('title')
    # obj = models.Book.objects.filter(title__startswith='g').values('title')

    #关联表查询
    # obj = models.Publish.objects.filter(book__title='鲁滨逊').values('name')
    # obj = models.Book.objects.filter(publisher__name='中信出版社').values('title')
    # obj = models.Book.objects.filter(title='鲁滨逊').values('publisher__name')

    #聚合查询和分组查询
    #聚合查询
    # obj = models.Book.objects.aggregate(Sum('price'),Max('price'),Min('price'))
    #分组查询
    # obj = models.Book.objects.values('publisher__name').annotate(Sum('price'))

    #F查询和Q查询
    # obj = models.Book.objects.all().update(price = F('price')+20)
    # Q查询
    obj = models.Book.objects.filter(Q(price__gt=30)&(Q(page_num=100)|Q(title='python')),color='red')
    print(obj)
    return HttpResponse('OK')


def ajax_index(req):
    return render(req,'ajax_index.html')

def ajax_receive(req):
    if req.method == 'POST':
        username = req.POST.get("username")
        if username == 'jason':
            return HttpResponse('1')
        else:
            return HttpResponse('0')
    return HttpResponse("ajax_get_ok")