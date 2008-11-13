from sbd.issue.models import Section, Article, Issue, PrintIssue
from django.contrib import admin

admin.site.register([Section, Issue, Article, PrintIssue])
