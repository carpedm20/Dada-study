from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import .views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studyplan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='core'),
)
