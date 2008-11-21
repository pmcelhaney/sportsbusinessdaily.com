from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^home/(?P<issue_date>\d{4}-\d{2}-\d{2})$', 'sbd.issue.views.home'),
    (r'^article/(?P<article_id>\d+)$', 'sbd.issue.views.single_article'),
    (r'^print-issue/(?P<issue_date>\d{4}-\d{2}-\d{2})$', 'sbd.issue.views.print_issue'),
)
