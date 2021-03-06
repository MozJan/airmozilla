from django.conf.urls.defaults import patterns, url
from django.views.generic.base import RedirectView
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^channels/(?P<channel_slug>[-\w]+)/$', views.home,
        name='home_channels'),
    url(r'^page/1/$', RedirectView.as_view(url='/'), name='first_page'),
    url(r'^page/(?P<page>\d+)/$', views.home, name='home'),
    url(r'^channels/(?P<channel_slug>[-\w]+)/page/(?P<page>\d+)/$',
        views.home, name='home_channels'),
    url(r'^channels/$', views.channels, name='channels'),
    url(r'^presenter/(?P<slug>[-\w]+)/$', views.participant,
        name='participant'),
    url(r'^presenter-clear/(?P<clear_token>[-\w]+)/$', views.participant_clear,
        name='participant_clear'),
    url(r'^login/$', views.page, name='login',
        kwargs={'template': 'main/login.html'}),
    url(r'^login-failure/$', views.page, name='login_failure',
        kwargs={'template': 'main/login_failure.html'}),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^calendar/data.json$', views.calendar_data, name='calendar_data'),
    url(r'^calendars/$', views.calendars, name='calendars'),
    url(r'^calendar/(company|contributors|public).ics$',
        views.events_calendar_ical, name='calendar_ical'),
    url(r'^feed/(company|public|private|contributors)?/?$',
        cache_page(views.EventsFeed(), 60 * 60),
        name='feed'),
    url(r'^feed/(?P<channel_slug>[-\w]+)/$',
        cache_page(views.EventsFeed(), 60 * 60),
        name='channel_feed_default'),
    url(r'^feed/(?P<channel_slug>[-\w]+)/'
        r'(?P<private_or_public>company|public|private|contributors)/?$',
        cache_page(views.EventsFeed(), 60 * 60),
        name='channel_feed'),
    url(r'^tagcloud/$', views.tag_cloud, name='tag_cloud'),
    url(r'^(?P<slug>[-\w]+)/$', views.EventView.as_view(),
        name='event'),
    url(r'^(?P<slug>[-\w]+)/video/$', views.EventVideoView.as_view(),
        name='event_video'),
)
