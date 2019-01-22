# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from SOD_LVM.models import *


# Create your models here.
# 任务模板
class JobTemplate(models.Model):
    COLORS = (
        ('StackStorm', 'StackStorm'),
        ('AnsibleTower', 'AnsibleTower'),

    )
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Name")
    orchtype = models.CharField(max_length=100, choices=COLORS, null=False, default='StackStorm',
                                verbose_name="Orchtype")

    def __init__(self, *args, **kwargs):
        super(JobTemplate, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    def __unicode__(self):
        return self.orchtype + ":" + self.name

    class Meta:
        db_table = 'jobtemplate'
        verbose_name = 'Job template'
        verbose_name_plural = 'Job templates'


class Orchestrator(models.Model):
    COLORS = (
        ('StackStorm', 'StackStorm'),
        ('AnsibleTower', 'AnsibleTower'),

    )
    id = models.CharField(max_length=100, primary_key=True)
    url = models.URLField(verbose_name='Url')
    orchtype = models.CharField(max_length=100, choices=COLORS, null=False, default='StackStorm',
                                verbose_name="Orchtype")
    datacenter = models.ForeignKey(DataCenter, verbose_name="Datacenter")
    username = models.CharField(max_length=30, verbose_name="Username")
    password = models.CharField(max_length=30, verbose_name="Password")
    lifecycle_state = models.ForeignKey(LifecycleState, verbose_name="Lifecycle_state")

    def __init__(self, *args, **kwargs):
        super(Orchestrator, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    def __unicode__(self):
        return self.datacenter.legacy_vpc_name + "->" + self.orchtype + "->" + self.url

    class Meta:
        db_table = 'orchestrator'
        verbose_name = 'Orchestrator'
        verbose_name_plural = 'Orchestrators'


class Schedule(models.Model):
    COLORS_Type = (
        ("daily", "daily"),
        ("weekly", "weekly"),
        ("monthly", "monthly"),
        ("onetime", "onetime"),
    )
    COLORS_Status = (
        ("Active", "Active"),
        ("Executed", "Executed"),
        ("Error", "Error"),
    )
    tenant = models.ForeignKey(Tenant, verbose_name='Tenant')
    system = models.ForeignKey(System, verbose_name='System')
    jobtemplatename = models.CharField(max_length=100, verbose_name='Jobtemplatename')
    type = models.CharField(max_length=100, choices=COLORS_Type, verbose_name='Type')
    request = models.TextField(verbose_name='Request')
    minute = models.IntegerField(verbose_name='Minute')
    hour = models.IntegerField(verbose_name='Hour')
    day = models.IntegerField(verbose_name='Day')
    date = models.IntegerField(verbose_name='Date')
    next_runt_ime = models.DateTimeField(verbose_name='Next runt ime')
    last_run_time = models.DateTimeField(verbose_name='Last run time')
    enabled = models.BooleanField(default=True, verbose_name='Enabled')
    status = models.CharField(max_length=100, choices=COLORS_Status, null=False, default="Active",
                              verbose_name='Status')
    error_message = models.TextField(verbose_name='Error message')

    def __init__(self, *args, **kwargs):
        super(Schedule, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    def __unicode__(self):
        return self.jobtemplatename

    class Meta:
        db_table = 'schedule'
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'


class Job(models.Model):
    COLORS = (
        ('New', "New"),
        ("Init", "Init"),
        ("Requested", "Requested"),
        ("Retrive_error", "Retrive_error"),
        ("Scheduled", "Scheduled"),
        ("Pending", "Pending"),
        ("Running", "Running"),
        ("Succeeded", "Succeeded"),
        ("Closed", "Closed"),
        ("Waiting", "Waiting"),
        ("Failed", "Failed"),
        ("Error", "Error"),
        ("Timeout", "Timeout"),
        ("Canceled", "Canceled"),
        ("Canceling", "Canceling"),
        ("Paused", "Paused"),
        ("Pausing", "Pausing"),
        ("Resuming", "Resuming"),
    )
    id = models.CharField(max_length=100, primary_key=True)
    jobtemplate = models.ForeignKey(JobTemplate, verbose_name='Jobtemplate')
    orchestrator = models.ForeignKey(Orchestrator, verbose_name='Orchestrator')
    executionid = models.CharField(max_length=100, verbose_name='Executionid')
    jobstatus = models.CharField(max_length=100, choices=COLORS, null=False, verbose_name='Jobstatus')
    schedule = models.ForeignKey(Schedule, verbose_name='Schedule')
    scheduletime = models.DateTimeField(verbose_name='Scheduletime')
    trigerat = models.DateTimeField(verbose_name='Trigerat')
    request = models.TextField(verbose_name='Request')
    response = models.TextField(verbose_name='Response')
    tenant = models.ForeignKey(Tenant, verbose_name='Tenant')
    resourceid = models.CharField(max_length=100, verbose_name='Resourceid')
    retrynum = models.IntegerField(verbose_name='Retrynum')

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid.uuid1()

    def __unicode__(self):
        return str(self.id) + "(" + self.jobtemplate.orchtype + ":" + self.jobtemplate.name + ")"

    class Meta:
        db_table = 'job'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
