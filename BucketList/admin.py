from __future__ import unicode_literals

from django.contrib import admin
from BucketList.models import User,ListItem,Profile,Leader



admin.site.register(Profile)
admin.site.register(ListItem)
admin.site.register(Leader)