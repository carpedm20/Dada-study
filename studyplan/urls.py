from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from board import views as b_views

STUDY = r'^s/(?P<study_group_id>\w+)/'

BOARD = STUDY + r'board/'
EVENT = STUDY + r'evnet/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studyplan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'core.views.index'),


    ###############
    # BOARD
    ###############
    url(BOARD + r'create/$', b_views.create_board, name='create_board'),
    url(BOARD + r'list/$', b_views.list_board, name='list_board'),
    url(BOARD + r'(?P<board_id>\d+)/create/$', b_views.create_post, name='create_post'),
    url(BOARD + r'(?P<board_id>\d+)/edit/(?P<post_id>\d+)$', b_views.edit_post, name='edit_post'),

    url(BOARD + r'(?P<board_id>\d+)/view/(?P<post_id>\d+)$', b_views.view_post, name='view_post'),


    url(r'^s/(?P<study_group_id>\w+)/event/', include('event.urls', namespace='event')),

    url(r'^s/', include('core.urls', namespace='core')),

    url(r'^school/', include('school.urls', namespace='school')),
    url(r'^account/', include('account.urls', namespace='account')),


    url(r'^chat/', include('chat.urls', namespace='chat')),

    (r'^summernote/', include('django_summernote.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
