from django.urls import path
from BucketList import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name='BucketList'

urlpatterns = [
	path('', views.home),
	url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^Calendar/$',views.Calendar,name='Calendar'),
    url(r'^upload/$', views.upload, name='upload')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
