from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'boottest/index.html')


def signin(request):
    return render(request, 'boottest/Signin.html')


def signup(request):
    return render(request, 'boottest/Signup.html')
