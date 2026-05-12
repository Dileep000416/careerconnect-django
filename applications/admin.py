from django.contrib import admin

from .models import Application,SavedJob


admin.site.register(Application)
admin.site.register(SavedJob)