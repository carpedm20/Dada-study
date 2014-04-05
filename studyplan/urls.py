from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studyplan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'core.views.index'),

    url(r'^study/', include('core.urls', namespace='core')),
    url(r'^school/', include('school.urls', namespace='school')),
    url(r'^account/', include('account.urls', namespace='account')),

    (r'^summernote/', include('django_summernote.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
