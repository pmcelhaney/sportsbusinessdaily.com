from django.shortcuts import render_to_response, get_object_or_404
from models import Article, Issue, PrintIssue

def single_article(request, article_id):
  a = get_object_or_404(Article, pk=article_id)
  return render_to_response('issue/article.html', {'article': a})
  
def print_issue(request, issue_date):
  issue = get_object_or_404(Issue, pk=issue_date)
  articles = issue.article_set.all().order_by('section','headline')
  i = 0
  for article in articles:
    i = i + 1
    article.number = i
  return render_to_response('issue/print_issue.html', {'print_issue': issue.printissue, 'articles': articles})