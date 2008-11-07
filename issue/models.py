from django.db import models

class Section(models.Model):
  name = models.CharField(max_length=200)
  
  def __unicode__(self):
    return self.name
  
class Article(models.Model):
  section = models.ForeignKey(Section)
  headline = models.CharField(max_length=200)
  mini_headline = models.CharField(max_length=200)
  body = models.TextField()
  issue_date = models.DateField()
  
  def __unicode__(self):
    return self.headline
  
