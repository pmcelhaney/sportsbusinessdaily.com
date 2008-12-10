from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^(?P<issue_date>\d{4}-\d{2}-\d{2})/$', 'sbd.issue.views.home'),
    (r'^article/(?P<article_id>\d+)$', 'sbd.issue.views.single_article'),
    (r'^(?P<issue_date>\d{4}-\d{2}-\d{2})/section/(?P<id>\d+)$', 'sbd.issue.views.section'),
    (r'^(?P<issue_date>\d{4}-\d{2}-\d{2})/print$', 'sbd.issue.views.print_issue'),
)
