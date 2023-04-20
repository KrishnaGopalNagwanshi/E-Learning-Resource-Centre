from django.shortcuts import render,redirect
from django.http import HttpResponse
from googlesearch import search
from pdfs.models import *
from .models import *
from videos.models import *
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
def index(request):
	
	pdfmodels=pdfsmodels.objects.all()
	return render(request,'index.html',{'pdf':pdfmodels})

def search1(request):
	show=[]
	pdfobj=pdfsmodels.objects.all()
	if request.method=='POST':
		key=request.POST['keyword']
		for i in pdfobj:
			if key.lower() in i.name or key.capitalize() in i.name:
				show.append(i)
			elif key.lower() in i.details or key.capitalize() in i.details:
				show.append(i)
		a=search(key,tld='com',num=20,stop=20,pause=2)

				

	return render(request,'index.html',{'show':show,'a':a})
def userhome(request):
	show=[]
	pdfobj=pdfsmodels.objects.all()
	if request.method=='POST':
		key=request.POST['keyword']
		for i in pdfobj:
			if key.lower() in i.name or key.capitalize() in i.name:
				show.append(i)
			elif key.lower() in i.details or key.capitalize() in i.details:
				show.append(i)
		a=search(key,tld='com',num=20,stop=20,pause=2)

				

	return render(request,'userhome.html',{'show':show,'a':a})

def  gsearch(request):
	if request.method=='POST':
		key=request.POST['keyword']
		a=search(key,tld='com',num=10,stop=10,pause=2)
		print(a)
	return render(request,'gsearch.html',{'a':a})



def register(request):
	if request.method=='POST':
		fname=request.POST['fn']
		lname=request.POST['ln']
		em=request.POST['eml']
		pwd=request.POST['passwd']
		uname=request.POST['eml']
		usrtype=request.POST['usertype']
		userobj=User(first_name=fname,last_name=lname,password=make_password(pwd),email=em,username=uname)
		userobj.save()

		probj=adprofile(user=userobj,utype=usrtype)
		probj.save()
	return render(request,'register.html')

def login_in(request):
	if request.method=='POST':
		usernm=request.POST['uname']
		pwd=request.POST['passwd']

		user=authenticate(username=usernm,password=pwd)
		if user:
			login(request,user)
			return render(request,'userhome.html')
		else:
			return redirect('/register/')
	return render(request,'login.html')
def myadmin(request):
	
	if request.method=='POST':
		usernm=request.POST['uname']
		pwd=request.POST['passwd']

		user=authenticate(username=usernm,password=pwd)
		if user:
			login(request,user)
			profileobj=adprofile.objects.get(user__username=request.user)
			if profileobj.utype=='Admin':
				return redirect('/adminhome/')
			else:
				return redirect('/')
				
		else:
			return HttpResponse("<h1>Invalid Credentials</h1>")
	return render(request,'myadmin.html')
def recent(request):
	pass
def adminhome(request):
	usersobj=User.objects.all()
	totaluser=usersobj.count()
	vobj=videosmodels.objects.all().count()
	pdfobj=pdfsmodels.objects.all().count()
	print(vobj)
	return render(request,'dashboard.html',{'usersobj':usersobj,'totaluser':totaluser,'vobj':vobj,'pdfobj':pdfobj})
def logout_call(request):
	logout(request)
	return redirect('/')

def clear(request):
	uobj=adprofile.objects.get(user__username=request.user)
	c=recentlog.objects.filter(added_by_id=uobj)
	c.delete()
	return render(request,'userhome.html')
