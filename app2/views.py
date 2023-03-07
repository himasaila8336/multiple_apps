from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app2_first(request):
    return HttpResponse('<h1> this is second first view function</h1>')
def app2_second(request):
    return HttpResponse('<h1> this is second view function</h1>')    