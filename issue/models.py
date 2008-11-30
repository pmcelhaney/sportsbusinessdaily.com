from django.db import models
import re




def int2roman(number):
  """ 
  convert an integer to a roman numeral
  Source: http://www.daniweb.com/code/snippet635.html
  """
  numerals = { 1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL", 50 : "L", 90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M" }
  result = ""
  for value, numeral in sorted(numerals.items(), reverse=True):
    while number >= value:
      result += numeral
      number -= value
  return result
  
class Section(models.Model):
  name = models.CharField(max_length=200)
  
  def __unicode__(self):
    return self.name
  
class Issue(models.Model):
  issue_date = models.DateField(primary_key=True)
  volume_number = models.IntegerField()
  issue_number = models.IntegerField()
  
  @property
  def volume_number_roman(self):
    return int2roman(self.volume_number)
  
  def __unicode__ (self):
    return self.issue_date.strftime('%A, %b %d, %Y')

class PrintIssue(models.Model):
  issue = models.OneToOneField(Issue,primary_key=True)
  top_story = models.TextField()
  headlines = models.TextField()
  quote_of_the_day = models.TextField()
  box1_header = models.CharField(max_length=50,blank=True)
  box1 = models.TextField()
  box2_header = models.CharField(max_length=50,blank=True)
  box2 = models.TextField()
  masthead = models.TextField()
  
  @property 
  def issue_date(self):
    return self.issue.issue_date
   
  @property      
  def issue_number(self):
  	return self.issue.issue_number    
  
  @property  
  def volume_number_roman(self):
    return self.issue.volume_number_roman
    
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