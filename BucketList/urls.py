from django.urls import path
from BucketList import views
from django.conf.urls import url


app_name='BucketList'

urlpatterns = [
	path('', views.home),
	url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^Calendar/$',views.Calendar,name='Calendar'),
]

