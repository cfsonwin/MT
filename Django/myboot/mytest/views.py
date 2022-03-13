from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, "mytemplate/user_page.html")


def t1(request):
    return HttpResponse("t1")


def t2(request):
    return HttpResponse("t2")


def t3(request):
    return HttpResponse("t3")


def t4(request):
    return HttpResponse("t4")
