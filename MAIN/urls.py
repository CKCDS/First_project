from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^jobtemplate/$", JobTemplateList.as_view()),
    url(r"^jobtemplate/(?P<pk>[0-9]+)/$", JobTemplateDetail.as_view()),
    url(r"^orchestrator/$", OrchestratorList.as_view()),
    url(r"^orchestrator/(?P<pk>[0-9]+)/$", OrchestratorDetail.as_view()),
    url(r"^schedule/$", ScheduleList.as_view()),
    url(r"^schedule/(?P<pk>[0-9]+)/$", ScheduleDetail.as_view()),
    url(r"^job/$", JobList.as_view()),
    url(r"^job/(?P<pk>[0-9]+)/$", JobDetail.as_view()),

]
