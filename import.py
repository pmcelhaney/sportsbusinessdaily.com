from django.conf import settings

import os

settings.configure(
        DEBUG = True,
        DATABASE_ENGINE = 'sqlite3',                    
        DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'sbd.db').replace('\\','/'),
)

from django.contrib.flatpages.models import *
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


def sections():
    print "\nSECTIONS"
    for record in csv_reader(open("data/departments.csv")):    
        if record["book"] == "SBD" and record["status"] == "active":
            section = Section(pk=record['departmentid'])
            section.name = record['department']
            section.rank = record['rank']
            print section
            section.save()

def issues():
    print "\nISSUES"
    for record in csv_reader(open("data/october_issues.csv")):
        issue = Issue(pk=parse_datetime(record['issuedate']))
        issue.volume_number = 12
        issue.issue_number = 11
        print issue
        issue.save()

def home_pages():
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


def print_issues():
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
        pi.box2_header = record['box2header']
        pi.box2 = record['box2']
        pi.masthead = record['masthead']
        print pi
        pi.save()
 

def articles(): 
    print "\nARTICLES" 
    for record in csv_reader(open("data/october_articles.csv")):
        if (record['department'] != ''):
            article = Article(pk=record['articleid'])
            article.issue = Issue(pk=parse_datetime(record['postdate']))
            article.section = Section(pk=record['department'])
            article.rank = record['rank'] or 0
            article.headline = record['headline']
            article.mini_headline = record['miniheadline']
            article.body = record['body']
            print article
            article.save()        

def sports():
    print "\nSPORTS" 
    for record in csv_reader(open("data/sports.csv")):
        sport = Sport(pk=record["sportid"])
        sport.name = record["sport"]
        print sport
        sport.save()

def companies():
    print "\nCompanies" 
    for record in csv_reader(open("data/companies.csv")):
        company = Company(pk=record["companyid"])
        company.name = record["company"]
        print company
        company.save()

def related_sports():
    print "\nRelated Sports"
    for record in csv_reader(open("data/october_relatedsportlookup.csv")): 
        article = Article.objects.get(pk=int(record['articleid']))
        sport = Sport.objects.get(pk=int(record['sportid']))
        article.sports.add(sport)
        print "[%s] %s" % (sport, article)
        article.save()


def related_companies():
    print "\nRelated Companies"
    for record in csv_reader(open("data/october_relatedcompanylookup.csv")): 
        article = Article.objects.get(pk=int(record['articleid']))
        company = Company.objects.get(pk=int(record['companyid']))
        article.companies.add(company)
        print "[%s] %s" % (company, article)
        article.save()        


def pages():
    print "\nPages"
    hard_urls = {
        '38' : '/faq',
        '83' : '/tos',
        '82' : '/privacy',
    }
    for record in csv_reader(open("data/pages.csv")):
        page_id = record["pageid"]
        if page_id in hard_urls:
            url = hard_urls[page_id]
        else:
            url = "/page/%s" % record["pageid"]
        
        page, created = FlatPage.objects.get_or_create(url=url)
        page.title = record["title"]
        page.content = record["body"]
        page.save()
        print page


pages()
sections()
issues()
home_pages()
print_issues()
articles()
sports()
companies()
related_sports()
related_companies()



    