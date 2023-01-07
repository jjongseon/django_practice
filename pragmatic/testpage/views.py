from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def testpage(request):
    return  render(request,'testpage/main.html')