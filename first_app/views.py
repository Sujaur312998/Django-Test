from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(reqest):
    diction={}
    return render(reqest,'first_app/index.html',context=diction)