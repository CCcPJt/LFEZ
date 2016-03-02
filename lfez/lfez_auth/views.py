#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.gengeric import View
from django.core.exceptions import PermissionDenied
from django.contrib import auth


class UserControl(View):
	def post(self, request, *args, **kwargs):
		slug = self.kwargs.get('slug')

        if slug == "login":
            return self.login(request)
	    elif slug == "logout":
            return self.logout(request)
        elif slug == "register":
            return self.register(request)
        elif slug == "changepassword":
            return self.changepassword(request)
        elif slug == "forgetpassword":
            return self.forgetpassword(request)
        elif slug == "changetx":
            return self.changetx(request)
        elif slug == "resetpassword":
            return self.resetpassword(request)

        raise PermissionDenied


    def get(self, request, *args, **kwargs):
        raise Http404


    def login(self, request):
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        user = auth.authenticate(username=username,password=password)

        errors = []

        if user is not None:
            auth.login(request, user)
        else:
            errors.append("用户名或密码不正确")

        return_msg = {'errors': errors}
        return HttpResponse(json.dumps(return_msg), content_type="application/json")


    def logout(self, request):
        if not request.user.is_authenticated():
                logger.error(u)
