from django.contrib import admin

from .models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name","init_date","end_date"]

class TaskAdmin(admin.ModelAdmin):
    list_display = ["id","project","description","end_date"]

admin.site.register(Project,ProjectAdmin)
admin.site.register(Task,TaskAdmin)
