from django.shortcuts import render_to_response, get_object_or_404
from models import Article, Issue, PrintIssue, Fixture

def home(request, issue_date):
  issue = get_object_or_404(Issue, pk=issue_date)	
  params = dict([(f.name, f.value) for f in Fixture.objects.all()])
  params['issue'] = issue.homepage
  params['articles'] = issue.article_set.all().order_by('section','headline')
  params['recent_issues'] = Issue.objects.all().order_by('-issue_date')[:10]
  return render_to_response('issue/home.html', params)
  
def single_article(request, article_id):
  article = get_object_or_404(Article, pk=article_id)
  issue = article.issue
  articles = issue.article_set.all().order_by('section','headline')
  articles_in_section = articles.filter(section=article.section)
  return render_to_response('issue/article.html', {'article': article, 'articles': articles, 'issue': issue.homepage, 'articles_in_section': articles_in_section })
  
def print_issue(request, issue_date):
  issue = get_object_or_404(Issue, pk=issue_date)
  articles = issue.article_set.all().order_by('section','headline')
  return render_to_response('issue/print_issue.html', {'print_issue': issue.printissue, 'articles': articles})