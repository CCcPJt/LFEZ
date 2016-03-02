from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def test_view(request):
	return render(request, 'forum/test.html')


def index(request):
	pass

def groups(request):
	pass

def activities(request):
	pass


def me(request):
	pass

