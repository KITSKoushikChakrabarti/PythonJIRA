from jira import JIRA
import getpass
 
pw = getpass.getpass()
jira = JIRA(auth=('chakrk03', pw) , options = {'server': 'https://jira.kfplc.com'})

# PARAMETER - pass a new CodeCut date to be put in new BAU release stories 
newCCDate = "27th Nov"

# get active sprint issues in Done status in a Project
issues_in_project = jira.search_issues('project=DRRR AND sprint not in closedSprints() AND sprint not in futureSprints() AND labels ="ATG11" AND labels ="BQUK" AND key=DRRR-437') # use key=DRRR-437 for testing only

print ('\n###### All ATG BAU issues in current sprint #####\n')

# --- tested and working fine ------
for value in issues_in_project:
        newSummary = value.fields.summary
        newSummary = newSummary.replace("13th Nov", newCCDate)
        newDesc = value.fields.description
        newDesc = newDesc.replace("13th Nov", newCCDate)
        jiraType = value.fields.issuetype
        newAssignee= value.fields.assignee
        newPriority= value.fields.priority
        storyPoint = value.fields.customfield_10002      
        newLabels = value.fields.labels  
        epicName = value.fields.customfield_10006     
               
        print('\n', value.key, newSummary, newDesc, jiraType,newAssignee, newPriority, newLabels, storyPoint, epicName) 

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
        
        #new_issue = jira.create_issue(project='DRRR', summary=newSummary, description=newDesc, issuetype=jiraType, assignee=newAssignee, priority=newPriority, labels=newLabels               
         )
        
        #print('\nNew issue created: ', new_issue)

        #jira.add_remote_link(value, new_issue)

       # newEpic = "Digital Releases - Wave 14"
       # new_issue.update(fields={'customfield_12360': newEpic})
 #For each of these issues Clone it (create a new issue)


#new_issue = jira.create_issue(project='DRRR', summary='New issue from jira-python', description='Sample description text', issuetype={'name': 'Bug'})