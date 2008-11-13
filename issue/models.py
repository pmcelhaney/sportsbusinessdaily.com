from django.db import models
import re

def string_to_image_name(s):
  non_letters = re.compile("[^A-Za-z0-9-\.\/]")
  return non_letters.sub("", s.replace(' ', '-')) + '.jpg'


  
class Section(models.Model):
  name = models.CharField(max_length=200)
  
  def __unicode__(self):
    return self.name
  
class Issue(models.Model):
  issue_date = models.DateField(primary_key=True)
  
  def __unicode__ (self):
    return self.issue_date.strftime('%A, %b %d, %Y')

class PrintIssue(models.Model):
  issue = models.OneToOneField(Issue)
  top_story = models.TextField()
  headlines = models.TextField()
  quote_of_the_day = models.TextField()
  volume_number = models.IntegerField()
  issue_number = models.IntegerField()
  box1_header = models.CharField(max_length=50)
  box1 = models.TextField()
  box2_header = models.CharField(max_length=50)
  box2 = models.TextField()
  masthead = models.TextField()
  
  
    
  
  def box1_header_image(self): 
    return string_to_image_name(self.box1_header)
  
  def box2_header_image(self):
    return string_to_image_name(self.box2_header)
  
  def __unicode__(self):
    return self.issue.__unicode__()
  
class Article(models.Model):
  issue = models.ForeignKey(Issue)
  section = models.ForeignKey(Section)
  headline = models.CharField(max_length=200)
  mini_headline = models.CharField(max_length=200)
  body = models.TextField()

  def __unicode__(self):
    return self.headline  