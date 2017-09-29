from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
# 使用 django 框架的自身鉴权
from django.contrib import auth
# 使用装配器进行 登录函数的限制
from django.contrib.auth.decorators import login_required

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
    # username = request.COOKIES.get('user', '') # 读取浏览器cookie
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user": username})