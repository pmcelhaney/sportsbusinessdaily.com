import pymssql
from issue.models import PrintIssue, Issue

con = pymssql.connect(user='sportsbusinessdaily',password='w=ucUkA3',host='hmnclustdb01',database='sportsbusinessdaily')
cursor = con.cursor()
sql = "select top 5 issueDate, cast(topStory as text) as topstory, cast(headlines as text) as headlines, cast(quote as text) as quote, box1header, box2header, cast(box1 as text) as box1, cast(box2 as text) as box2, volume, number, swapcolumns, cast(masthead as text) as masthead from printissues where issueDate < '2008-11-01' order by issueDate desc"

cursor.execute(sql)

print cursor.rowcount

first_issue = cursor.fetchall()[0]

issue = Issue()
issue.issue_date = first_issue[0]
issue.save()

print_issue = PrintIssue()
print_issue.issue = issue
print_issue.top_story = first_issue[1]
print_issue.headlines = first_issue[2]
print_issue.quote_of_the_day = first_issue[3]
print_issue.volume_number = 15
print_issue.issue_number = 99
print_issue.save()

print print_issue
