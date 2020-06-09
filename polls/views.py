# 어떤 데이터를 보여줄까
#from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
	return HttpResponse('Hello, which data do you wanna know?')
