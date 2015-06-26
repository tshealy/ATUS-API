from django.contrib import admin

# Register your models here.
from .models import HouseholdList, People, Respondents, Activity, ActivityList

class BookmarkAdmin(admin.ModelAdmin):
    fields=['url', 'description', 'tags', 'user', 'breveurl']
    list_display = ('url', 'description', 'created_at', 'last_updated')

admin.site.register(HouseholdList)
admin.site.register(People)
admin.site.register(Respondents)
admin.site.register(Activity)
admin.site.register(ActivityList)
