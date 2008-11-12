from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^article/(?P<article_id>\d+)$', 'sbd.issue.views.single_article'),
)
