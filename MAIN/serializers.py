from rest_framework import serializers

from .models import *


class JobTemplateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = JobTemplate
        fields = '__all__'


class OrchestratorSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Orchestrator
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Schedule
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Job
        fields = '__all__'
