import re
from django.shortcuts import redirect
from django.urls import reverse

class AdLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('AdLoginMiddleware')
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('url: ', request.path)

        # if already login
        urllist = ['/Admin/signin/', '/Admin/dosignin/', '/Admin/signout/', '/Admin/signup/', '/Admin/signupcheck/']
        if re.match(r'^/Admin', request.path) and (request.path not in urllist):
            if 'already_login' not in request.session:
                return redirect(reverse('mAD_signin'))
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
