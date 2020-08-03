# Developed by Koushik - Apr 2020
# Purpose: Gets all Open issues assigned to me in JIRA 
from jira import JIRA
import getpass
 
# login to JIRA using username and password
print ("Enter credentials to login to JIRA:")
user = input("Username: ")
pw = getpass.getpass()
jira = JIRA(auth=(user, pw) , options = {'server': 'https://jira.kfplc.com'})


print (' ------  Summary of all my OPEN issues in JIRA  ----- ')
cnt = 0
for issue in jira.search_issues('project=DRRR and assignee = currentUser() and status != DONE ',maxResults=30):
   print('[{}: {}]'.format(issue.key, issue.fields.summary))
   cnt = cnt + 1   
print('Total items found:  ',cnt)