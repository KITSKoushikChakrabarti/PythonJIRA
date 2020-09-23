
# Developed by Koushik - Aug 2020
# Purpose: Clone JIRA issues from a given JQL resultset

from jira import JIRA
import getpass

## Use of Python Functions
def CloneJIRAIssue(issue,projKey):
    newSummary = issue.fields.summary # title 
    # newSummary = newSummary.replace("Sonarqube","Nexus")  # modify if needed
    newDesc = issue.fields.description # description 
    jiraType = issue.fields.issuetype.name
    newAssignee= issue.fields.assignee
    newPriority= issue.fields.priority.name        
    newLabels = issue.fields.labels        
    new_issue = projKey + '-' + issue.key + '-001' # testing
    # new_issue = jira.create_issue(project=projKey, summary=newSummary, 
        # description=newDesc, issuetype={'name': jiraType}, assignee={'name': newAssignee},
        # priority= {'name': newPriority}, labels=newLabels)    
    return new_issue

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
projectKey = input("\nEnter the JIRA Board or Project Name where the issues will be cloned: ")

for issue in issueList:
    print('\nCloning {}: {}'.format(issue.key, issue.fields.summary))
    newIssue = CloneJIRAIssue(issue, projectKey)   # functiona call with params
    print('New Issue: ', newIssue)
    # for each issue perform the cloning action here
    # newSummary = value.fields.summary
    # newDesc = value.fields.description
    # jiraType = value.fields.issuetype.name
    # newAssignee= value.fields.assignee.name
    # newPriority= value.fields.priority.name        
    # newLabels = value.fields.labels        
    # new_issue = jira.create_issue(project=projectKey, summary=newSummary, 
    #     description=newDesc, issuetype={'name': jiraType}, assignee={'name': newAssignee},
    #     priority= {'name': newPriority}, labels=newLabels)

