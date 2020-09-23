
# Developed by Koushik - Sep 2020
# Purpose: Clone JIRA Initiatives down till Epic level
# Current JIRA hierarchy is (Iinitiatives--> Deliverables --> Epics -->Stories)
from jira import JIRA
import getpass

######### Use of Python Functions ##########
def CloneJIRAIssue(issue,projKey):
    newSummary = issue.fields.summary # title 
    # newSummary = newSummary.replace("Sonarqube","Nexus")  # modify if needed
    newDesc = issue.fields.description # description 
    jiraType = issue.fields.issuetype.name
    newAssignee= issue.fields.assignee
    newPriority= issue.fields.priority.name        
    newLabels = issue.fields.labels        
    # new_issue = projKey + '-' + issue.key + '-001' # testing
    new_issue = jira.create_issue(project=projKey, summary=newSummary, 
        description=newDesc, issuetype={'name': jiraType}, assignee={'name': newAssignee},
        priority= {'name': newPriority}, labels=newLabels)    
    return new_issue
############ End of Function ################


# login to JIRA using username and password
print("\n----- This Python program will clone a JIRA Initiative recursively into Deliverables & Epics ----- ")
print("\nEnter credentials to login to JIRA:")
user = input("Username: ")
pw = getpass.getpass()
jira = JIRA(auth=(user, pw), options={'server': 'https://jira.kfplc.com'})

# use this code to get more than 50 results in search issues in an interative loop
block_size = 200
# block_num = 0
cntDelivTotal = 0
cntEpicTotal = 0
jqlSortOrder = ' ORDER BY Key ASC'    
issueID = 1
while issueID != '0':        
    # start_idx = block_num*block_size
    # Enter a JQL query to generate the output resultset which will be the source of issues to be cloned  
    issueID = input("\nEnter a JIRA Initiative (type 0 to exit): ")
    if issueID == '0':        
        break  
    # ask which board the issues should be cloned into
    projectKey = input("\nEnter JIRA Board or Project Name where issues will be cloned (e.g. DQC / DJE): ")
    jqlDemand = '"Parent Link"=' + issueID;  # e.g. "Parent Link" = ED-5

    delivList = jira.search_issues(jqlDemand + jqlSortOrder, 0, block_size)   # "Parent Link" = ED-5 ORDER BY Key ASC  
    cntDelivTotal = len(delivList) # get count of Deliverables
    print('Total Deliverables: ', cntDelivTotal)
    if cntDelivTotal == 0:        
        break            
    # block_num += 1
    for deliv in delivList:   # Loop through deliverables
        # Clone the deliverable
        print('\nCloning deliverable [{}]: {}'.format(deliv.key, deliv.fields.summary))
        newDeliv = CloneJIRAIssue(deliv, projectKey)   # function call with params
        print('New Issue created: ', newDeliv)

        jqlEpic = '"Parent Link"=' + deliv.key         
        epicList = jira.search_issues(jqlEpic + jqlSortOrder, 0, block_size)        
        cntEpicTotal = len(epicList) # get count of Epics
        print('\tTotal epics: ', cntEpicTotal)
        if cntEpicTotal == 0:          
            continue    
        for epic in epicList: # Loop through epics
            # Clone the epic
            print('\n\tCloning epic [{}]: {}'.format(epic.key, epic.fields.summary))
            newEpic = CloneJIRAIssue(epic, projectKey)   # function call with params
            print('\tNew Issue created: ', newEpic)

    print('\nCloning completed successfully.')

