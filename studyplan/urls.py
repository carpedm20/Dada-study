from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import study

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studyplan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', study.views.index);

    url(r'^study/', include('study.urls')),
    url(r'^school/', include('school.urls')),
    url(r'^aaccount/', include('account.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
