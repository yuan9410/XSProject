from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# Create your views here.
def index(request):
    # 请求路径和请求方法
    print(request.path, request.method)
    # 请求头的源信息和GET请求参数(查询参数)
    print(request.META)
    print(request.GET)
    # POST请求参数(表单参数)
    print(request.POST)

    # return HttpResponse('<h1>您好</h1>')
    # return JsonResponse ({'name':'jay','age':18})
    return render(request,'art/list.html',context={'name':'jay','age':18})