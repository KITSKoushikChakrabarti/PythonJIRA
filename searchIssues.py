# Developed by Koushik - Apr 2020
# Purpose: Search for issues in current sprint 
from jira import JIRA
import getpass
 
# login to JIRA using username and password
print ("Enter credentials to login to JIRA:")
user = input("Username: ")
pw = getpass.getpass()
jira = JIRA(auth=(user, pw) , options = {'server': 'https://jira.kfplc.com'})


# get active sprint issues  in a Project - ignore 'and status != Done' 
#issues_in_proj = jira.search_issues('project=DRRR')
issues_in_project = jira.search_issues('project=DRRR and sprint not in closedSprints() AND sprint not in futureSprints() ')

print ('-------- All issues in current sprint -------')
for value in issues_in_project:
        print(value.key, ':', value.fields.summary, ':(',value.fields.assignee, ')') 


# Summaries of my last 3 reported issues
print ('------ Summary of my last 3 reported issues --------')
for issue in jira.search_issues('reporter = currentUser() order by created desc', maxResults=3):
    print('{}: {}'.format(issue.key, issue.fields.summary))


# To be tested
print ('------ Count of open issues in active sprint ------- ')
openIssues = jira.search_issues('project=DRRR and sprint not in closedSprints() AND sprint not in futureSprints() AND  status != Done',  startAt=0, 
                   maxResults=0, 
                   json_result=True)
#print ('Total = ', openIssues.raw); raw

# This script shows how to connect to a Jira instance with a
# username and password over HTTP BASIC authentication.

######### Get Top 3 issues natching results #############

from collections import Counter
from jira import JIRA
jira = JIRA(basic_auth=("admin", "admin"))  # a username/password tuple

# Get the mutable application properties for this server (requires
# jira-system-administrators permission)
props = jira.application_properties()

# Find all issues reported by the admin
issues = jira.search_issues("assignee=admin")

# Find the top three projects containing issues reported by admin
top_three = Counter([issue.fields.project.key for issue in issues]).most_common(3)