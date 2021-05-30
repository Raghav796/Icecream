from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
   return render(request,'contact.html')
def scoops(request):
   return render(request,'scoops.html')
def tubs(request):
   return render(request,'tubs.html')
def bars(request):
   return render(request,'bars.html')
def cones(request):
   return render(request,'cones.html')
