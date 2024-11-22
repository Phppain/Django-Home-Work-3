from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse(render(request, 'login.html'))

def home(request):
    return HttpResponse(render(request, 'home.html'))

def base(request):
    return HttpResponse(render(request, 'base.html'))
