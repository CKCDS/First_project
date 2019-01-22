# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from django.apps import AppConfig

from .models import *


class MainConfig(AppConfig):
    name = 'MAIN'


class JobTemplateFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = JobTemplate
        fields = '__all__'


class OrchestratorFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Orchestrator
        fields = '__all__'


class ScheduleFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Schedule
        fields = '__all__'


class JobFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Job
        fields = '__all__'
