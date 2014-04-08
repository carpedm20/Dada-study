from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studyplan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='home'),

    url(r'^calendar/$', views.view_calendar, name='view_calendar'),
    url(r'^create/$', views.create_study_group, name='create_study_group'),
    url(r'^join/$', views.join_study_group, name='join_study_group'),

    url(r'^(?P<unique_id>\w+)/$', views.view_study_group, name='view_study_group'),

    url(r'^group/board/edit/$', include('django_summernote.urls')),

    url(r'^articles/comments/', include('django.contrib.comments.urls')),
)
