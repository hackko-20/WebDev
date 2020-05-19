from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import ListItem,Profile,Leader,Notes,Announcements
from .forms import Userform
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import operator
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import F
import random


class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		item_all = Profile.objects.all()
		data2=[]
		data=[]
		labels=[]
		member_list=[]
		for it in item_all:
			data2.append(0)
			data2.append(it.ctask_jan)
			data2.append(it.ctask_feb)
			data2.append(it.ctask_mar)
			data2.append(it.ctask_apr)
			data2.append(it.ctask_may)
			data2.append(it.ctask_june)
			data2.append(it.ctask_july)
			data2.append(it.ctask_aug)
			data2.append(it.ctask_sept)
			data2.append(it.ctask_oct)
			data2.append(it.ctask_nov)
			data2.append(it.ctask_dec)
			data2.append(0)
			temp=[it.mem,'JAN','FEB','MAR','APR','MAY','JUNE','JULY','AUG','SEPT','OCT','NOV','DEC',' ']
			labels = labels + temp
			data.append(0)
			data.append(it.task_jan)
			data.append(it.task_feb)
			data.append(it.task_mar)
			data.append(it.task_apr)
			data.append(it.task_may)
			data.append(it.task_june)
			data.append(it.task_july)
			data.append(it.task_aug)
			data.append(it.task_sept)
			data.append(it.task_oct)
			data.append(it.task_nov)
			data.append(it.task_dec)
			data.append(0)
		datagone = {
			"labels":labels,
			"y_axis1":data,
			"y_axis2":data2,
		}
		return Response(datagone)

def addNotes(request):
	new_note = Notes(notesid=request.user,content=request.POST['notes'])
	new_note.save()
	return HttpResponseRedirect('/')

def addAnnounce(request):
	new_announce = Announcements(announceid=request.user,content=request.POST['announces'])
	new_announce.save()
	return HttpResponseRedirect('/')

def Calendar(request):
	return render(request,'BucketList/change_list.html',{})

def home(request, leadsignedin={}):
	context={
	'leadsignedin':False
	}
	if request.user.is_authenticated:
		notes = Notes.objects.filter(notesid=request.user.id)
		announce = Announcements.objects.filter(announceid=request.user.id)
		all_member= Profile.objects.filter(memberid__id=request.user.id)
		all_items = ListItem.objects.filter(team__id=request.user.id)
		allitems = all_items.filter(status="Incomplete")
		TeamLeader= Leader.objects.filter(leaderid__id=request.user.id)
		context.update(leadsignedin)
		return render(request,'BucketList/home.html',{'all':allitems,'all_members':all_member,'teamleader':TeamLeader,'leadsignedin':leadsignedin,'notifs':all_items, 'notes':notes, 'announce':announce})
	else:
		return render(request,'BucketList/home.html',{})

def add(request):
	new_item= ListItem(content=request.POST['content'],member=request.POST['member'],deadline=request.POST['deadline'],team=request.user,month=request.POST['month'])
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
	if(month == "JAN"):
		Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['member']).update(task_jan=F('task_jan')+1)
		
	if(month == "FEB"):
		Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['member']).update(task_feb=F('task_feb')+1)
		
	if(month == "MAR"):
		Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['member']).update(task_mar=F('task_mar')+1)
		
	if(month == "APR"):
		Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['member']).update(task_apr=F('task_apr')+1)
		
	if(month == "MAY"):
		Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['member']).update(task_may=F('task_may')+1)
		
	if(month == "JUNE"):
		Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['member']).update(task_june=F('task_june')+1)
		
	if(month == "JULY"):
		Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['member']).update(task_july=F('task_july')+1)
		
	if(month == "AUG"):
		Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['member']).update(task_aug=F('task_aug')+1)
		
	if(month == "SEPT"):
		Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['member']).update(task_sept=F('task_sept')+1)
		
	if(month == "OCT"):
		Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['member']).update(task_oct=F('task_oct')+1)
		
	if(month == "NOV"):
		Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['member']).update(task_nov=F('task_nov')+1)
		
	if(month == "DEC"):
		Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['member']).update(task_dec=F('task_dec')+1)
		
	return HttpResponseRedirect('/')
	
	
def addMember(request):
	new_mem= Profile(mem=request.POST['memname'],memberid=request.user)
	new_mem.save()
	return HttpResponseRedirect('/')

def addLeader(request):
	leader=Leader(Group_leader=request.POST['Leader'],leader_pin="abcd",leaderid=request.user)
	all_member= Profile.objects.filter(memberid__id=request.user.id)
	flag=0;
	for member in all_member:
		if(leader.Group_leader == member.mem):
			leader.save()
			messages.info(request,"Your pin is abcd")
			return HttpResponseRedirect('/')
			flag=1;
	if(flag==0):
		messages.info(request,"Leader could not be added as it was assigned to a non-existent member")
		return HttpResponseRedirect('/')

def delete(request,item_id):
	item_d= ListItem.objects.get(id=item_id)
	month = item_d.month
	if(month == "JAN"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item_d.member).update(task_jan=F('task_jan')-1)
		
	if(month == "FEB"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item_d.member).update(task_feb=F('task_feb')-1)
		
	if(month == "MAR"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item_d.member).update(task_mar=F('task_mar')-1)
		
	if(month == "APR"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item_d.member).update(task_apr=F('task_apr')-1)
		
	if(month == "MAY"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item_d.member).update(task_may=F('task_may')-1)
		
	if(month == "JUNE"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item_d.member).update(task_june=F('task_june')-1)
		
	if(month == "JULY"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item_d.member).update(task_july=F('task_july')-1)
		
	if(month == "AUG"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item_d.member).update(task_aug=F('task_aug')-1)
		
	if(month == "SEPT"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item_d.member).update(task_sept=F('task_sept')-1)
		
	if(month == "OCT"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item_d.member).update(task_oct=F('task_oct')-1)
		
	if(month == "NOV"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item_d.member).update(task_nov=F('task_nov')-1)
		
	if(month == "DEC"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item_d.member).update(task_dec=F('task_dec')-1)
	item_d.delete()
	return HttpResponseRedirect('/')

def complete(request,item_id):
	item= ListItem.objects.get(id=item_id)
	item.status="Completed :)"
	item.save()
	if(item.month == "JAN"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(ctask_jan=F('ctask_jan')+1)
	if(item.month == "FEB"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(ctask_feb=F('ctask_feb')+1)
	if(item.month == "MAR"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(ctask_mar=F('ctask_mar')+1)
	if(item.month == "APR"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(ctask_apr=F('ctask_apr')+1)
	if(item.month == "MAY"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(ctask_may=F('ctask_may')+1)
	if(item.month == "JUNE"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(ctask_june=F('ctask_june')+1)
	if(item.month == "JULY"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(ctask_july=F('ctask_july')+1)
	if(item.month == "AUG"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(ctask_aug=F('ctask_aug')+1)
	if(item.month == "SEPT"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(ctask_sept=F('ctask_sept')+1)
	if(item.month == "OCT"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(ctask_oct=F('ctask_oct')+1)
	if(item.month == "NOV"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(ctask_nov=F('ctask_nov')+1)
	if(item.month == "DEC"):
		Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(ctask_dec=F('ctask_dec')+1)

	return HttpResponseRedirect('/')

def change(request,item_id):
	flag=0;
	members=Profile.objects.filter(memberid__id=request.user.id)
	new_mem=request.POST['memchange']
	for member in members:
		if(new_mem == member.mem):
			item = ListItem.objects.get(id=item_id)
			name = item.member
			month = item.month
			if(item.month == "JAN"):
				Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(task_jan=F('task_jan')-1)
			if(item.month == "FEB"):
				Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(task_feb=F('task_feb')-1)
			if(item.month == "MAR"):
				Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(task_mar=F('task_mar')-1)
			if(item.month == "APR"):
				Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(task_apr=F('task_apr')-1)
			if(item.month == "MAY"):
				Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(task_may=F('task_may')-1)
			if(item.month == "JUNE"):
				Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(task_june=F('task_june')-1)
			if(item.month == "JULY"):
				Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(task_july=F('task_july')-1)
			if(item.month == "AUG"):
				Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(task_aug=F('task_aug')-1)
			if(item.month == "SEPT"):
				Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(task_sept=F('task_sept')-1)
			if(item.month == "OCT"):
				Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(task_oct=F('task_oct')-1)
			if(item.month == "NOV"):
				Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(task_nov=F('task_nov')-1)
			if(item.month == "DEC"):
				Profile.objects.filter(memberid__id=request.user.id,mem=item.member).update(task_dec=F('task_dec')-1)
			if(item.month == "JAN"):
				Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['memchange']).update(task_jan=F('task_jan')+1)
			if(item.month == "FEB"):
				Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['memchange']).update(task_feb=F('task_feb')+1)
			if(item.month == "MAR"):
				Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['memchange']).update(task_mar=F('task_mar')+1)
			if(item.month == "APR"):
				Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['memchange']).update(task_apr=F('task_apr')+1)
			if(item.month == "MAY"):
				Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['memchange']).update(task_may=F('task_may')+1)
			if(item.month == "JUNE"):
				Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['memchange']).update(task_june=F('task_june')+1)
			if(item.month == "JULY"):
				Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['memchange']).update(task_july=F('task_july')+1)
			if(item.month == "AUG"):
				Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['memchange']).update(task_aug=F('task_aug')+1)
			if(item.month == "SEPT"):
				Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['memchange']).update(task_sept=F('task_sept')+1)
			if(item.month == "OCT"):
				Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['memchange']).update(task_oct=F('task_oct')+1)
			if(item.month == "NOV"):
				Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['memchange']).update(task_nov=F('task_nov')+1)
			if(item.month == "DEC"):
				Profile.objects.filter(memberid__id=request.user.id,mem=request.POST['memchange']).update(task_dec=F('task_dec')+1)	
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

def signasmember(request):
	membersignin=False
	memberpin=request.POST.get('memberpin')
	member= Profile.objects.get(memberid__id=request.user.id,mem_username=request.POST['name'])
	if(memberpin == member.memberpin):
		membersignin=True
		items_list=ListItem.objects.filter(member=member.mem,status="Incomplete")
		notes = Notes.objects.all()
		announces = Announcements.objects.all()
		notifs = ListItem.objects.filter(member=member.mem)
		context={'memsignedin':membersignin,'member':member,'item_list':items_list,'notes':notes,'announces':announces,'notifs':notifs}

		return render(request,'BucketList/member.html',context)
	else:
		messages.info(request,"Wrong pin!")
		return HttpResponseRedirect('/')

def signup(request):
	members = Profile.objects.get(memberid__id=request.user.id,mem=request.POST['memname'])
	if( members ):
		members.mem_username = request.POST.get('memusername')
		members.memberpin=request.POST.get('mempassword')
		members.save()
		messages.info(request,"You can sign in now!")
		return HttpResponseRedirect('/')
	else:
		messages.info(request,"No such member exists in the group")
		return HttpResponseRedirect('/')



