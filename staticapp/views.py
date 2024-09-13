from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'staticapp/index.html')

def home1(request):
    return render(request,'staticapp/about.html')

def abd(request):
    return render(request,'staticapp/vision.html')

def abe(request):
    return render(request,'staticapp/program.html')