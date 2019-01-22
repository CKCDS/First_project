# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


# Register your models here.
class JobTemplateAdmin(admin.ModelAdmin):
    list_display = ( "id", "name", "orchtype",)
    fields = ("id", "name", "orchtype",)


class OrchestratorAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "orchtype", "datacenter", "username", "password", "lifecycle_state",)
    fields = ( "url", "orchtype", "datacenter", "username", "password", "lifecycle_state",)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("id",
    "tenant", "system", "jobtemplatename", "type", "request", "minute", "hour", "day", "date", "next_runt_ime",
    "last_run_time", "enabled", "status", "error_message",)
    fields = (
                    "tenant", "system", "jobtemplatename", "type", "request", "minute", "hour", "day", "date",
                    "next_runt_ime",
                    "last_run_time", "enabled", "status", "error_message",)


class JobAdmin(admin.ModelAdmin):
    list_display = (
    "id", "jobtemplate", "orchestrator", "executionid", "jobstatus", "schedule", "scheduletime", "trigerat",
    "request", "response", "tenant", "resourceid", "retrynum",)
    fields = ("jobtemplate", "orchestrator", "executionid", "jobstatus", "schedule", "scheduletime", "trigerat",
        "request", "response", "tenant", "resourceid", "retrynum",)


admin.site.register(JobTemplate, JobTemplateAdmin)
admin.site.register(Orchestrator, OrchestratorAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Job, JobAdmin)
