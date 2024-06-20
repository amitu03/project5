from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def amit(request):
    return HttpResponse('amitu and mental')
def mental(request):
    return HttpResponse('mental and amitu')
