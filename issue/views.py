from django.shortcuts import render_to_response, get_object_or_404
from models import Article

def single_article(request, article_id):
  a = get_object_or_404(Article, pk=article_id)
  return render_to_response('issue/article.html', {'article': a})