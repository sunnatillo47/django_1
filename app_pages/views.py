from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def page1(requests):
	return HttpResponse('PAGE 1')

def page2(requests):
	return HttpResponse('PAGE 2')

def page3(requests):
	return HttpResponse('PAGE 3')

def page4(requests):
	return HttpResponse('PAGE 4')

def page5(requests):
	return HttpResponse('PAGE 5')