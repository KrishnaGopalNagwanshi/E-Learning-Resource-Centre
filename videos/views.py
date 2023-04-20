from django.shortcuts import render,redirect
from .models import*
from googlesearch import search
from django.contrib import messages
from searchme.models import *
# Create your views here.
def videos_index(request):
	uobj=adprofile.objects.get(user__username=request.user)
	rcobjs=recentlog.objects.filter(added_by_id=uobj.id)
	recent=[]
	for i in rcobjs:
		recent.append(i)

	return render(request,'videos.html',{'recent':recent})

def searchvideos(request):
	uobj=adprofile.objects.get(user__username=request.user)
	show=[]
	uobj=adprofile.objects.get(user__username=request.user)
	rcobjs=recentlog.objects.filter(added_by_id=uobj.id)
	recent=[]
	for i in rcobjs:
		recent.append(i)

	pdfobj=videosmodels.objects.all()
	if request.method=='POST':
		key=request.POST['keyword']
		rl=recentlog(added_by=uobj,log=key).save()
		for i in pdfobj:
			if key.lower() in i.name or key.capitalize() in i.name:
				show.append(i)
			elif key.lower() in i.details or key.capitalize() in i.details:
				show.append(i)
		a=search(key+'videos tutorial',tld='com',num=10,stop=10,pause=2)
	return render(request,'videos.html',{'show':show,'a':a,'recent':recent})

def addvideo(request):
	if request.method=='POST':
		a=request.POST['name']
		b=request.POST['details']
		c=request.POST['remark']
		d=request.FILES['file']
		pdfobj=videosmodels(name=a,details=b,rating=c,file=d)
		pdfobj.save()
		messages.success(request,'Data successfully Added !!')
		return redirect('/adminhome/')
	return render(request,'videoadd.html')