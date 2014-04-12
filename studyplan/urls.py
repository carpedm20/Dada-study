from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from core import views as c_views
from board import views as b_views
from event import views as e_views

STUDY = r'^s/(?P<study_group_id>\w+)/'

BOARD = STUDY + r'board/'
EVENT = STUDY + r'event/'

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
    url(BOARD + r'(?P<board_id>\d+)/(?P<post_id>\d+)/edit/$', b_views.edit_post, name='edit_post'),
    url(BOARD + r'(?P<board_id>\d+)/(?P<post_id>\d+)/delete/$', b_views.delete_post, name='delete_post'),
    url(BOARD + r'(?P<board_id>\d+)/(?P<post_id>\d+)/comment/$', b_views.create_comment, name='create_comment'),
    url(BOARD + r'(?P<board_id>\d+)/(?P<post_id>\d+)/comment/(?P<comment_id>\d+)/delete/$', b_views.delete_comment, name='delete_comment'),

    url(BOARD + r'(?P<board_id>\d+)/view/(?P<post_id>\d+)$', b_views.view_post, name='view_post'),


    ###############
    # EVENT
    ###############

    url(EVENT + r'view/$', e_views.view_calendar, name='view_calendar'),

    url(EVENT + r'get/$', e_views.get_event_as_json, name='get_event'),
    #url(EVENT + r'view/$', e_views.view_calendar, name='view_calendar'),
    url(EVENT + r'edit/$', e_views.edit_event, name='edit_event'),
    url(EVENT + r'delete/$', e_views.delete_event, name='delete_event'),
    url(EVENT + r'create/$', e_views.create_event, name='create_event'),


    url(r'^s/', include('core.urls', namespace='core')),

    url(r'^school/', include('school.urls', namespace='school')),
    url(r'^account/', include('account.urls', namespace='account')),


    url(r'^chat/', include('chat.urls', namespace='chat')),

    (r'^summernote/', include('django_summernote.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
