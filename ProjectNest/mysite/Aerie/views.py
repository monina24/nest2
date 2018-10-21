from django.http import HttpResponse
from Aerie.models import Nest
from Aerie.models import Account
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

import json

# Create your views here.
@require_http_methods(["GET"])
def home(request):
	return render(request,"home.html")

@require_http_methods(["GET"])
def myNest(request):
	return render(request,"nest.html")

@require_http_methods(["GET"])
def createAccount(request):
	return render(request, "createAccount.html")

@require_http_methods(["GET"])
def login(request):
	return render(request, "login.html")

@require_http_methods(["GET"])
def welcome(request):
	return render(request, "welcome.html")

@require_http_methods(["GET"])
def findNest(request):
	return render(request, "findNest.html")

@require_http_methods(["GET"])
def createNest(request):
	return render(request, "createNest.html")



# implement a function that will take a GET REQUEST
# from a user pressing the "My Nest" button
# and looks in the database 

@require_http_methods(["POST"])
@csrf_exempt
def createNestAPI(request):
	
	nest_name = request.POST.get('nest_name', None)
	description = request.POST.get('description', None)
	team_members = request.POST.get('team_members', None)
	nest = Nest(nest_name = nest_name, description=description, team_members=team_members)
	nest.save()
	return render(request,"myNest.html")


@csrf_exempt
@require_http_methods(["POST"])
def createAccountAPI(request):
	
	acc_name = request.POST.get('account_name')
	password = request.POST.get('password')
	account = Account(account_name=acc_name, password=password)
	account.save()
	return render(request,"welcome.html")


@csrf_exempt
@require_http_methods(["POST"])
def loginAPI(request):
	
	acc_name = request.POST.get('account_name')
	password = request.POST.get('password')
	listAcc = Account.objects.filter(account_name=acc_name,password=password)
	
	if(len(listAcc) == 0):
		return render(request, "login.html")
	else:
		return render(request,"welcome.html")


@csrf_exempt
@require_http_methods(["POST"])
def myNestAPI(request):
	# look up username field in list of nests
	# on matches, return first one and show it
	return ''


@csrf_exempt
@require_http_methods(["POST"])
def findNestAPI(request):
	# load all available nests
	allNests = Nest.objects.all()
	render(request, "findNests.html", allNests)











