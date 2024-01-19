from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ab(self):
	return HttpResponse("Django")

def home(request):
	return render(request,'html/home.html')

def sample(request):
	return render(request,'html/sample.html')