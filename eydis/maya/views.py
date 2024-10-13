from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request, 'home.html')

def myname_index(request):
    return render (request, 'myname.html')

def mygroup_index(request):
    return render (request, 'mygroup.html')

def myage_index(request):
    return render (request, 'myage.html')

def common(request):
    return render (request, 'common.html')