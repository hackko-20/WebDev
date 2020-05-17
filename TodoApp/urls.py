"""TodoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from BucketList.views import change,complete,add,delete,sortbydead,sortbymem,unsort,addMember,addLeader,signasleader,ChartData,addNotes,addAnnounce
from BucketList import views
from django.conf.urls import url,include

app_name='BucketList'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('BucketList.urls')),
    path('add/', add),
    path('addMember/',addMember),
    path('addLeader/',addLeader),
    path('delete/<int:item_id>/',delete),
    path('complete/<int:item_id>/',complete),
    path('change/<int:item_id>/',change),
    path('sort1/',sortbydead,name="sortbydead"),
    path('sort2/',sortbymem,name="sortbymem"),
    path('unsort/',unsort,name="unsort"),
    path('addNotes/',addNotes),
    path('addAnnounce/',addAnnounce),
    url(r'^$',views.home,name='home'),
    url(r'^special/',views.special,name='special'),
    url(r'^BucketList/',include('BucketList.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^chart/getdata/$',ChartData.as_view(), name='get-chart-data'),
    url(r'^signasleader/$', views.signasleader, name='signasleader'),

]
