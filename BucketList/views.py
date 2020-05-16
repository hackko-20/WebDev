from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import ListItem,Profile,Leader,GraphMem,No_task
from .forms import Userform
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import operator
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import F


class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		itemall = No_task.objects.all()
		members = GraphMem.objects.all()
		item_count = members.count()
		data=[]
		labels=[]
		member_list=[]
		for j in members:
			member_list.append(j.name)
		for i in range(item_count):
			temp=[member_list[i],'JAN','FEB','MAR','APR','MAY','JUNE','JULY','AUG','SEPT','OCT','NOV','DEC',' ']
			labels = labels + temp

		for item in itemall:
			data.append(0)
			data.append(item.task_jan)
			data.append(item.task_feb)
			data.append(item.task_mar)
			data.append(item.task_apr)
			data.append(item.task_may)
			data.append(item.task_june)
			data.append(item.task_july)
			data.append(item.task_aug)
			data.append(item.task_sept)
			data.append(item.task_oct)
			data.append(item.task_nov)
			data.append(item.task_dec)
			data.append(0)
		datagone = {
			"labels":labels,
			"y_axis":data,
		}
		return Response(datagone)

def Calendar(request):
	members=GraphMem.objects.all()
	return render(request,'BucketList/change_list.html',{'members':members})

def home(request, leadsignedin={}):
	context={
	'leadsignedin':False
	}
	if request.user.is_authenticated:
		all_member= Profile.objects.filter(memberid__id=request.user.id)
		all_items = ListItem.objects.filter(team__id=request.user.id)
		allitems = all_items.filter(status="Incomplete")
		TeamLeader= Leader.objects.filter(leaderid__id=request.user.id)
		context.update(leadsignedin)
		return render(request,'BucketList/home.html',{'all':allitems,'all_members':all_member,'teamleader':TeamLeader,'leadsignedin':leadsignedin,'notifs':all_items})
	else:
		return render(request,'BucketList/home.html',{})

def add(request):
	new_item= ListItem(content=request.POST['content'],member=request.POST['member'],deadline=request.POST['deadline'],team=request.user)
	memb= GraphMem.objects.get(memid__id=request.user.id,name=request.POST['member'])
	all_member= Profile.objects.filter(memberid__id=request.user.id)
	flag=0;
	for member in all_member:
		if(new_item.member == member.mem):
			new_item.save()
			flag=1;
	if(flag==0):
		messages.info(request,"Work could not be added as it was assigned to a non-existent member")
		return HttpResponseRedirect('/')
	month = request.POST['month']
	temp = No_task.objects.filter(taskid=memb)
	if(not temp):
		graphmem = No_task(taskid=memb)
		graphmem.save()
	if(month == "JAN"):
		No_task.objects.filter(taskid=memb).update(task_jan=F('task_jan')+1)
		
	if(month == "FEB"):
		No_task.objects.filter(taskid=memb).update(task_feb=F('task_feb')+1)
		
	if(month == "MAR"):
		No_task.objects.filter(taskid=memb).update(task_mar=F('task_mar')+1)
		
	if(month == "APR"):
		No_task.objects.filter(taskid=memb).update(task_apr=F('task_apr')+1)
		
	if(month == "MAY"):
		No_task.objects.filter(taskid=memb).update(task_may=F('task_may')+1)
		
	if(month == "JUNE"):
		No_task.objects.filter(taskid=memb).update(task_june=F('task_june')+1)
		
	if(month == "JULY"):
		No_task.objects.filter(taskid=memb).update(task_july=F('task_july')+1)
		
	if(month == "AUG"):
		No_task.objects.filter(taskid=memb).update(task_aug=F('task_aug')+1)
		
	if(month == "SEPT"):
		No_task.objects.filter(taskid=memb).update(task_sept=F('task_sept')+1)
		
	if(month == "OCT"):
		No_task.objects.filter(taskid=memb).update(task_oct=F('task_oct')+1)
		
	if(month == "NOV"):
		No_task.objects.filter(taskid=memb).update(task_nov=F('task_nov')+1)
		
	if(month == "DEC"):
		No_task.objects.filter(taskid=memb).update(task_dec=F('task_dec')+1)
		
	return HttpResponseRedirect('/')
	


def addMember(request):
	new_mem= Profile(mem=request.POST['memname'],memberid=request.user)
	new_mem.save()
	new_graphmem = GraphMem(memid=request.user,name=request.POST['memname'])
	new_graphmem.save()
	return HttpResponseRedirect('/')

def addLeader(request):
	leader=Leader(Group_leader=request.POST['Leader'],leaderid=request.user,leader_pin="abcd")
	all_member= Profile.objects.filter(memberid__id=request.user.id)
	flag=0;
	for member in all_member:
		if(leader.Group_leader == member.mem):
			leader.save()
			messages.info(request,"Your pin is abcd.")
			return HttpResponseRedirect('/')
			flag=1;
	if(flag==0):
		messages.info(request,"Leader could not be added as it was assigned to a non-existent member")
		return HttpResponseRedirect('/')

def delete(request,item_id):
	item_d= ListItem.objects.get(id=item_id)
	memobj = GraphMem.objects.get(memid__id=request.user.id,name=item_d.member)
	memobj.delete()
	item_d.delete()

	return HttpResponseRedirect('/')

def complete(request,item_id):
	item_d= ListItem.objects.get(id=item_id)
	item_d.status="Completed :)"
	item_d.save()
	return HttpResponseRedirect('/')

def change(request,item_id):
	flag=0;
	members=Profile.objects.filter(memberid__id=request.user.id)
	new_mem=request.POST['memchange']
	for member in members:
		if(new_mem == member.mem):
			item_d= ListItem.objects.filter(id=item_id).update(member=request.POST['memchange'])
			flag=1;
	if(flag==0):
		messages.info(request,"Member is not a part of the team!")
	return HttpResponseRedirect('/')

def sortbydead(request):
	all_member= Profile.objects.filter(memberid__id=request.user.id)
	TeamLeader= Leader.objects.filter(leaderid__id=request.user.id)
	stuff = ListItem.objects.filter(team__id=request.user.id) 
	allitems = stuff.filter(status="Incomplete")
	all_items = allitems.order_by('deadline')
	return render(request,'BucketList/home.html',{'all':all_items,'all_members':all_member,'notifs':stuff,'teamleader':TeamLeader})

def sortbymem(request):
	all_member= Profile.objects.filter(memberid__id=request.user.id)
	TeamLeader= Leader.objects.filter(leaderid__id=request.user.id)
	stuff = ListItem.objects.filter(team__id=request.user.id)
	allitems = stuff.filter(status="Incomplete")
	all_items = allitems.order_by('member')
	return render(request,'BucketList/home.html',{'all':all_items,'all_members':all_member,'notifs':stuff,'teamleader':TeamLeader})

def unsort(request):
	all_member= Profile.objects.filter(memberid__id=request.user.id)
	TeamLeader= Leader.objects.filter(leaderid__id=request.user.id)
	all_items=ListItem.objects.filter(team__id=request.user.id)
	allitems = all_items.filter(status="Incomplete")
	return render(request,'BucketList/home.html',{'all':allitems,'all_members':all_member,'notifs':all_items,'teamleader':TeamLeader})

def addnotif(request):
	new_item= ListNotif(task=request.POST['task'],member2=request.POST['member2'],status=request.POST['status'])
	new_item.save()
	return HttpResponseRedirect('/')

     
@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = Userform(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered=True
		else:
			print(user_form.errors)
	else:
		user_form = Userform()
	return render(request,'BucketList/registrations.html',{'user_form':user_form,'registered':registered})

def user_login(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user:
			login(request,user)
			return HttpResponseRedirect(reverse('home'))
		else:
			messages.info(request,"Wrong username/password!")
			return render(request,'BucketList/login.html', {})
	else:
		return render(request,'BucketList/login.html', {})

def signasleader(request):
	leadersignin=False
	leaderpin=request.POST.get('leaderpin')
	leader= Leader.objects.get(leaderid__id=request.user.id)
	if(leaderpin == leader.leader_pin):
		leadersignin=True
		context={'leadsignedin':leadersignin}
		response=home(request, context)
		return response
	else:
		messages.info(request,"Wrong pin!")
		return HttpResponseRedirect('/')