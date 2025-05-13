from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, firstname, lastname):
    #return HttpResponse("Hello World!") #Question 2-1
    return HttpResponse(f"Hello, {firstname} {lastname}") #Question 2-2