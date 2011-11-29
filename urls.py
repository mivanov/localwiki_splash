from django.conf.urls.defaults import *
import members

from basic.blog.feeds import BlogPostsFeed

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.create_update import create_object
from contributors.models import LicenseAgreement

admin.autodiscover()

class FullBodyFeed(BlogPostsFeed):
    def item_description(self, item):
        return item.body

feeds = {
    'latest': FullBodyFeed,
}

from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    #(r'^$', direct_to_template, {'template': 'index.html'}),
    url(r'^$', direct_to_template, {'template': 'new_splash.html'}, name='home'),
    url(r'^install/$', direct_to_template, {'template': 'install.html'}, name='install'),

    (r'^signup_thanks', direct_to_template, {'template': 'signup_thanks.html'}),
    (r'^pilot_recommend_thanks', direct_to_template, {'template': 'pilot_recommend_thanks.html'}),
    (r'^faq', direct_to_template, {'template': 'faq.html'}),
    (r'^about', direct_to_template, {'template': 'about.html'}),

    (r'^signup/$', 'members.views.signup'),
    (r'^pilot_recommendation/$', 'members.views.pilot_recommendation'),
    (r'^blog/', include('basic.blog.urls')),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', 
        {'feed_dict': feeds}),
    (r'^comments/', include('django.contrib.comments.urls')),
    
    (r'^cla/$', create_object, { 'model': LicenseAgreement, 'post_save_redirect': '/cla/thanks/'}),
    (r'^cla/thanks/$', direct_to_template, { 'template': 'contributors/thanks.html'}),
    
    (r'^polls/', include('polls.urls')),   

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
