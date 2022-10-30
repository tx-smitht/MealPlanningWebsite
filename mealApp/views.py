
import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request):
    sOutput = 'Hello World!'
    return render(request, 'mealApp/index.html')