from sbd.issue.models import Section, Article, Issue, PrintIssue, HomePage, Fixture
from django.contrib import admin

admin.site.register([PrintIssue, HomePage, Fixture])

class SectionAdmin(admin.ModelAdmin):
  list_display = ('name', 'rank')
  
admin.site.register(Section, SectionAdmin)


class IssueAdmin(admin.ModelAdmin):
  date_hierarchy = 'issue_date'
 
admin.site.register(Issue, IssueAdmin)

class ArticleAdmin(admin.ModelAdmin):
  list_display = ['headline', 'section', 'issue_date']
  list_filter = ('section',)
  search_fields = ('headline', 'body')
  
admin.site.register(Article, ArticleAdmin)
	