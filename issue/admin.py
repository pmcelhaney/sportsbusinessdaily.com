from sbd.issue.models import Section, Article, Issue, PrintIssue, HomePage, Fixture
from django.contrib import admin

admin.site.register([Article, PrintIssue, HomePage, Fixture])

class SectionAdmin(admin.ModelAdmin):
  list_display = ('name', 'rank')
  
admin.site.register(Section, SectionAdmin)


class IssueAdmin(admin.ModelAdmin):
  date_hierarchy = 'issue_date'
 

admin.site.register(Issue, IssueAdmin)