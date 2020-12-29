from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print('第一个视图')
    return HttpResponse('页面')