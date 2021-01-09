from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home</h1>')

def aboutPage(request):
    return HttpResponse('<h1>Page was found,  ABOUT </h1>')    

