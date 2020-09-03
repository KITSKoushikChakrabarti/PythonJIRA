
# Developed by Koushik - Aug 2020
# Purpose: Clone JIRA issues from a given JQL resultset

from jira import JIRA
import getpass

# login to JIRA using username and password
print("----- This program clones JIRA issues from a given JQL query resultset ----- ")
print("\nEnter credentials to login to JIRA:")
user = input("Username: ")
pw = getpass.getpass()
jira = JIRA(auth=(user, pw), options={'server': 'https://jira.kfplc.com'})

# Enter a JQL query to generate the output resultset which will be the source of issues to be cloned  
jql = input("\nEnter a JQL query in proper format: ")

# run the JQL to get the resultset
issueList = jira.search_issues(jql) 

print("\nCount of issues from this JQL: ", len(issueList), '\n')

# ask which board the issues should be cloned into
projectName = input("\nEnter the JIRA Board or Project Name where the issues will be cloned: ")

for issue in issueList:
    print('Cloning {}: {}'.format(issue.key, issue.fields.summary))
    # for each issue perform the cloning action here
    # newSummary = value.fields.summary
    # newDesc = value.fields.description
    # jiraType = value.fields.issuetype.name
    # newAssignee= value.fields.assignee.name
    # newPriority= value.fields.priority.name        
    # newLabels = value.fields.labels        
    # new_issue = jira.create_issue(project=projectName, summary=newSummary, 
    #     description=newDesc, issuetype={'name': jiraType}, assignee={'name': newAssignee},
    #     priority= {'name': newPriority}, labels=newLabels)
