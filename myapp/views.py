from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testfn(request):
    return HttpResponse("hi")
def newfn(request):
    return HttpResponse("hi this a new page") 
def  funhtml1(request):
    return render(request,'test.html') 
def funnhtml2(request):
    return render(request,'new.html')  
def funhtml3(request):
    return render(request,'new3.html')      

