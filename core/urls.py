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
    url(r'^group/event/create/$', views.create_study_group, name='create_event'),
)
