from __future__ import unicode_literals

from django.contrib import admin
from BucketList.models import User,ListItem,Profile,Leader,GraphMem,No_task


# Register your models here.

'''class EventAdmin(admin.ModelAdmin):
	list_display = ['day', 'end_time', 'notes']
	change_list_template = 'BucketList/change_list.html'

	def changelist_view(self, request, extra_context=None):
		after_day = request.GET.get('day__gte',None)
		extra_context = extra_context or {}

		if not after_day:
			d = datetime.date.today()
		else:
			try:
				split_after_day = after_day.split('-')
				d = datetime.date(year=int(split_after_day[0]),month=int(split_after_day[1]),day=1)
			except:
				d = datetime.date.today()

		previous_month = datetime.date(year=d.year, month=d.month, day=1)
		previous_month = previous_month - datetime.timedelta(days=1)
		previous_month = datetime.date(year=previous_month.year, month=previous_month.month, day=1)

		last_day = calendar.monthrange(d.year, d.month)
		next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])
		next_month= next_month + datetime.timedelta(days=1)
		next_month = datetime.date(year=next_month.year, month=next_month.month, day=1)

		extra_context['previous_month'] = reverse('admin:BucketList_event_changelist') + '?day__gte=' + str(previous_month)
		extra_context['next_month'] = reverse('admin:BucketList_event_changelist') + '?day__gte=' + str(next_month)
		cal = HTMLCalendar()
		html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
		html_calendar = html_calendar.replace('<td', '<td width="150" height="150" ')
		extra_context['calendar'] = mark_safe(html_calendar)
		return super(EventAdmin, self).changelist_view(request, extra_context)'''

admin.site.register(GraphMem)
admin.site.register(No_task)
admin.site.register(Profile)
admin.site.register(ListItem)
admin.site.register(Leader)