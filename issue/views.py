from django.shortcuts import render_to_response, get_object_or_404
from models import Article, Issue, PrintIssue, Fixture, Section

def home(request, issue_date):
  issue = get_object_or_404(Issue, pk=issue_date)	
  params = dict([(f.name, f.value) for f in Fixture.objects.all()])
  params['issue'] = issue
  params['articles'] = issue.article_set.all().order_by('section')
  params['recent_issues'] = Issue.objects.all().order_by('-issue_date')[:10]
  return render_to_response('issue/home.html', params)
  
def single_article(request, article_id):
  article = get_object_or_404(Article, pk=article_id)
  issue = article.issue
  return render_to_response('issue/article.html', {
    'article': article, 
    'issue': issue, 
    'articles_in_section': issue.articles.filter(section=article.section), 
    'recent_issues': Issue.objects.all().order_by('-issue_date')[:10],
  })
  
def print_issue(request, issue_date):
  issue = get_object_or_404(Issue, pk=issue_date)
  articles = issue.article_set.all().order_by('section','headline')
  return render_to_response('issue/print_issue.html', {'print_issue': issue.printissue, 'articles': articles})
  

def section(request, issue_date, id): 
  issue = get_object_or_404(Issue, pk=issue_date)	
  section = get_object_or_404(Section, pk=id)
  articles_in_issue = issue.article_set.all().order_by('section')
  articles_in_section = articles_in_issue.filter(section=section)
  article = articles_in_section[0]
  return render_to_response('issue/section.html', {
    'article': article, 
    'articles': articles_in_issue, 
    'issue': issue, 
    'articles_in_section': articles_in_section, 
    'recent_issues': Issue.objects.all().order_by('-issue_date')[:10],
    
  })