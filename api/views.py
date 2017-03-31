from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .models import User

def index(req):
		return HttpResponse('hello~~ %s')

def detail(req, qid):
		a = User.objects.all()
		return JsonResponse({'data': a[0].name})
