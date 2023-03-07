from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse


def app1_first(request):
    return HttpResponse('<h1> this is first view function </h1>')
def app1_second(request):
    return HttpResponse('<h1> this is second view function </h1>')    