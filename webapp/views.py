from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def principal(request):
    return HttpResponse('Hola mundo desde django ')