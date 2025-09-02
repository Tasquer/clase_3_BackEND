from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vista1(request):
    return HttpResponse("<h1>rama1-Vista1</h1><p>Hola desde rama1/Vista1</p>")

def vista2(request):
    return HttpResponse("<h1>rama1 - Vista2</h1><p>Hola desde rama1/Vista2</p>")
