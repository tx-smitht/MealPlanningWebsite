from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    sOutput = 'Hello World!'
    return HttpResponse(sOutput)