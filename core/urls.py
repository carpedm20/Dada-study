from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studyplan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='home'),

    url(r'^group/create/$', views.create_study_group, name='create_study_group'),

    url(r'^group/event/create/$', views.create_event, name='create_event'),

    url(r'^group/event/calendar/$', views.view_calendar, name='view_calendar'),
    url(r'^group/event/get_event.json$', views.get_event_as_json, name='get_event_as_json'),

    url(r'^group/board/edit/$', include('django_summernote.urls')),
)
