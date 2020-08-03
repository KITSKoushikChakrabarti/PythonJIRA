# Developed by Koushik - Apr 2020
# Purpose: Clone Sprint stories from a search result
from jira import JIRA
import getpass

# login to JIRA using username and password
print("Enter credentials to login to JIRA:")
user = input("Username: ")
pw = getpass.getpass()
jira = JIRA(auth=(user, pw), options={'server': 'https://jira.kfplc.com'})

# pass a new code cut date to be put in new BAU release stories 
newCCDate = input("Enter new code-cut date (format: dd-MMM, example: 23-JAN")

# get active sprint issues in Done status in a Project
issues_in_project = jira.search_issues('project=DRRR AND sprint  in openSprints() AND labels ="ATG11" AND labels ="BQUK" ') # use key=DRRR-437 for testing only

# --- tested and working fine ------
#  --- replace 22nd Jan with the current sprint CC-date  ------
print ('\n------ Cloning all done issues from current sprint into backlog -------\n')
for value in issues_in_project:
        newSummary = value.fields.summary
        newSummary = newSummary.replace("22nd Jan", newCCDate)
        newDesc = value.fields.description
        newDesc = newDesc.replace("22nd Jan", newCCDate)
        jiraType = value.fields.issuetype.name
        newAssignee= value.fields.assignee.name
        newPriority= value.fields.priority.name        
        newLabels = value.fields.labels        
        ##newEpic = "Digital Releases - Wave 14"
        #newEpic2 = value.fields.cf[10016].name
        
        #print('\n', value.key, newSummary, newDesc, jiraType,newAssignee, newPriority, newLabels, newEpic) 

        #jira_dict_convert = {
        #'project': {'key': 'DRRR'},
        #'summary': newSummary,
        #'description': newDesc,
        #'assignee': {'name': newAssignee},
        #'priority': {'name': newPriority},
        #'issuetype': {'name': jiraType},  
        #'labels' : newLabels,
        #'reporter': {'name': 'User2@example.com'},                  
        #'issuelinks': [{"inwardIssue": {'key':existing_issue_key}}],
        #'customfield_12761': SomeCustomFieldValue,
        #'customfield_12360': newEpic,
        #}
    #newID = jira.create_issue(jira_dict_convert)
    #print('\nNew issue created: ', newID)
        
        new_issue = jira.create_issue(project='DRRR', summary=newSummary, description=newDesc, issuetype={'name': jiraType}, assignee={'name': newAssignee}, priority= {'name': newPriority}, labels=newLabels
        )

        print('\nNew issue created: ', new_issue)
