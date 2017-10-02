from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
# 使用 django 框架的自身鉴权
from django.contrib import auth
# 使用装配器进行 登录函数的限制
from django.contrib.auth.decorators import login_required
# 分页
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.shortcuts import render, get_object_or_404

from sign.models import Event, Guest

def index(request):
    # return HttpResponse("Hello django!")
    return render(request, "index.html")


def login_action(request):
    if  request.method == "POST":
        username = request.POST.get('username', '')
        pwd = request.POST.get('password', '')

        # 使用django 的用户鉴权机制
        user = auth.authenticate(username=username, password=pwd)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username
            response =  HttpResponseRedirect("/event_manage")
            return  response
        else:
            return render(request, "index.html", {'error': 'username or password error! '})

        # 笨方法
        # if username == 'admin' and pwd == 'admin':
        #     response = HttpResponseRedirect("/event_manage")
        #     # response.set_cookie('user', username, 3600) # cookie
        #     request.session['user'] = username  # 将 session 信息记录到浏览器
        #     return response
        # else:
        #     return render(request, "index.html", {'error': 'username or password error! '})
    else:
        return render(request, "index.html", {'error': 'http method must be POST! '})


@login_required
def event_manage(request):
    '''
    发布会管理
    '''

    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user": username, "events": event_list})


@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=search_name)

    return render(request, "event_manage.html", {"user": username, "events": event_list})


@login_required
def guest_manage(request):
    username = request.session.get("user", '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果超出最 大页数的范围，抛 EmptyPage 异常，返回最后一页面的数据。
        contacts = paginator.page(paginator.num_pages)

    return render(request, "guest_manage.html", {"user": username, "guests": contacts})


@login_required
def search_phone(request):
    username = request.session.get('user', '')
    search_phone = request.GET.get("phone", "")
    guest_list = Guest.objects.filter(phone__contains=search_phone)
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果超出最 大页数的范围，抛 EmptyPage 异常，返回最后一页面的数据。
        contacts = paginator.page(paginator.num_pages)


    return render(request, "guest_manage.html", {"user": username, "guests": contacts})


@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html', {'event': event})


@login_required
def sign_index_action(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    phone = request.POST.get('phone', '')

    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event':event, 'hint':'phone error.'})

    result = Guest.objects.filter(phone= phone, event_id=event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'event id or phone error.'})

    result = Guest.objects.get(phone= phone, event_id=event_id)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'user has sign in.'})
    else:
        Guest.objects.filter(phone=phone, event_id=event_id).update(sign = '1')
        return render(request, 'sign_index.html', {'event': event, 'hint': 'sign in success!', 'guest':result})


@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index')
    return response
