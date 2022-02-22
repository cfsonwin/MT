from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'boottest/index.html')

def link1(request):
    return render(request, 'boottest/Signin.html')

def myform(request):
    return render(request, 'boottest/MyForm.html')