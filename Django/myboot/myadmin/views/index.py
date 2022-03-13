from django.shortcuts import render, redirect
from django.urls import reverse

from myadmin.models import Administrator
from myadmin.util import pw_hash_salt


# Create your views here.
def index(request):
    return render(request, 'myadmin/index.html')


def do_signin(request):
    try:
        Ad = Administrator.objects.get(Email=request.POST['inputEmail'])
        if Ad.u_status != 0:
            context = {"info": "login failed! Administrator account not available",
                       "status": 0,
                       }
            return render(request, 'myadmin/Signin.html', context)
        if Ad.u_password == pw_hash_salt(request.POST['inputPassword'], Ad.pw_salt):
            request.session['already_login'] = Ad.toDict()
            return redirect(reverse('mAD_index'))
        else:
            context = {"info": "login failed! Email account not exist or password wrong.",
                       "status": 0,
                       }
            return render(request, 'myadmin/Signin.html', context)
    except Exception as err:
        print(err)
        context = {"info": "login failed! Email account not exist or password wrong.",
                   "status": 0,
                   }
        return render(request, 'myadmin/Signin.html', context)


def signin_form(request):
    return render(request, 'myadmin/Signin.html')


def sign_out(request):
    del request.session['already_login']
    return redirect(reverse('mAD_signin'))
