
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django!")


#BELOW is Old Code
#from django.shortcuts import render

# Create your views here.
