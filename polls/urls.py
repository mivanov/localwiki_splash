from django.conf.urls.defaults import patterns, include, url
from polls.models import Poll
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^(?P<poll_id>\d+)/$', 'polls.views.form'),
    (r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    url(r'^thanks/$', direct_to_template, { 'template': 'polls/thanks.html' }, name="poll_thanks"),
)
