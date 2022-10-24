from http.client import HTTPResponse
import imp
from re import X
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculate():
    x = 1 
    y = 2
    return X

def say_hello(request):
    x = calculate()
    return render(request , "hello.html",context={'name' : ''})