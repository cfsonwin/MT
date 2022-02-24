from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import User

# Create your views here.
def show(request):
    users = User.objects
    u_list = users.all()
    context = {'userlist':u_list}
    return render(request, 'myadmin/user/show.html', context)


def add(request):
    return render(request, 'myadmin/show.html')


def insert(request):
    return render(request, 'myadmin/show.html')


def delete(request, u_id):
    return render(request, 'myadmin/show.html')


def edit(request, u_id):
    return render(request, 'myadmin/show.html')


def update(request, u_id):
    return render(request, 'myadmin/show.html')
