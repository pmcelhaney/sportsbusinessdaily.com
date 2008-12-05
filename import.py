from django.conf import settings

import os

settings.configure(
    DEBUG = True,
    DATABASE_ENGINE = 'sqlite3',          
    DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'sbd.db').replace('\\','/'),
)

from issue.models import *

import csv
from datetime import *

class csv_reader:
  def __init__(self, file):
    self.reader = csv.reader(file)
    columns = self.reader.next()
    self.column_map = dict([(columns[i].lower(), i) for i in range(0, len(columns))])
  
  def __iter__(self):
    return self
    
  def next(self):
    self.current = self.reader.next()
    return self
  
  def __getitem__(self, name):
    value = self.current[self.column_map[name]]
    if "(null)" == value:
      value = ""
    return unicode(value, 'utf-8')

  def columns(self):
    return self.column_map


def parse_datetime(str):
  date_part = str.split(' ')[0]
  return datetime.strptime(date_part, '%m/%d/%Y')
  

print "\nSECTIONS"
for record in csv_reader(open("data/departments.csv")):  
  section = Section(pk=record['departmentid'])
  section.name = record['department']
  print section
  section.save()

print "\nISSUES"
for record in csv_reader(open("data/october_issues.csv")):
  issue = Issue(pk=parse_datetime(record['issuedate']))
  issue.volume_number = 12
  issue.issue_number = 11
  print issue
  issue.save()

print "\nHOME PAGES"  
for record in csv_reader(open("data/october_issues.csv")):
  issue = Issue(pk=parse_datetime(record['issuedate']))
  try:
  	hp = issue.homepage
  except HomePage.DoesNotExist:
  	hp = HomePage(issue=issue)
  hp.top_story = record['homepage_topstory']
  hp.headlines = record['homepage_headlines']
  hp.quote_of_the_day = record['homepage_quote']
  print hp
  hp.save()


print "\nPRINT ISSUES"  
for record in csv_reader(open("data/october_printissues.csv")):
  issue = Issue(pk=parse_datetime(record['issuedate']))
  try:
  	pi = issue.printissue
  except PrintIssue.DoesNotExist:
  	pi = PrintIssue(issue=issue)
  pi.top_story = record['topstory']
  pi.headlines = record['headlines']
  pi.quote_of_the_day = record['quote']
  pi.box1_header = record['box1header']
  pi.box1 = record['box1'] 
  if "(null)" != record['box1']:
  	pi.box1 = "" 
  pi.box2_header = record['box2header']
  pi.box2 = record['box2']
  if "(null)" != record['box2']:
  	 pi.box2 = "" 
  print pi
  pi.save()
 
 
print "\nARTICLES" 
for record in csv_reader(open("data/october_articles.csv")):
  if (record['department'] != '(null)'):
    article = Article(pk=record['articleid'])
    article.issue = Issue(pk=parse_datetime(record['postdate']))
    article.section = Section(pk=record['department'])
    article.headline = record['headline']
    article.mini_headline = record['miniheadline']
    article.body = record['body']
    print article
    article.save()    
