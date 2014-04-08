from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studyplan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^create/$', views.create_event, name='create_event'),
    url(r'^calendar/$', views.view_calendar, name='view_calendar'),
    url(r'^get_event.json$', views.get_event_as_json, name='get_event_as_json'),
)
