from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def main(request):
    return  render(request,'searchapp/main.html')

def testpage(request):
    return  render(request,'testpage/main.html')