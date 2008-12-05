from sbd.issue.models import Section, Article, Issue, PrintIssue, HomePage, Fixture
from django.contrib import admin

admin.site.register([Section, Issue, Article, PrintIssue, HomePage, Fixture])
