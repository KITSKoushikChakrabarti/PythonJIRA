
# Developed by Koushik - Sep 2020
# Purpose: Create Demand/Initiative summary report

from jira import JIRA
import getpass

# login to JIRA using username and password
print("----- This python program will create a Demand/Initiative Summary Report (html format) for a given initiative ID ----- ")
print("\nEnter credentials to login to JIRA:")
user = input("Username: ")
pw = getpass.getpass()
jira = JIRA(auth=(user, pw), options={'server': 'https://jira.kfplc.com'})

# Enter a JQL query to generate the output resultset which will be the source of issues to be cloned  
jql = input("\nEnter an Initiative or Demand ID: ")
jqlDemand = '"Parent Link"=' + jql;

# run the JQL to get child issues (Epics) resultset for that Demand
#epicList = jira.search_issues(jqlDemand) 

# use this code to get more than 50 results in search issues in an interative loop
block_size = 100
block_num = 0
cntEpicDone = 0
cntEpicTotal = 0
cntIssueTotal = 0
cntIssueDone = 0
while True:
    start_idx = block_num*block_size
    epicList = jira.search_issues(jqlDemand, start_idx, block_size)    
    cntEpicTotal = len(epicList) # save the Epic Total for display
    if len(epicList) == 0:
        # Retrieve issues until there are no more to come
        break    
    # print("\nCount of Epics in this demand: ", len(epicList), '\n')            
    block_num += 1
    for epic in epicList:
        # print('ID: {}, Summary: {}'.format(epic.key, epic.fields.summary))
        # print("Status: ", epic.fields.status.name)  #status
        print('\nEpic: {}'.format(epic.key))        
        jqlEpic = '"Parent Link"=' + epic.key;    
        if(epic.fields.status.name == "Done"):
            cntEpicDone += 1 # save the epic done count for display
        issueList = jira.search_issues(jqlEpic, 0, 100)
        # print("Count of issues in this Epic: ", len(issueList), '\n')
        cntIssueTotal = len(issueList) # save the Issue Total for display
        cntIssueDone = 0
        for issue in issueList:
            if(issue.fields.status.name == "Done"):
                cntIssueDone += 1 # save the issue done count for display
            # print('Issue: {}'.format(issue.key)) 
            try:
                percent = round(float(cntIssueDone/cntIssueTotal)*100,2);
            except ZeroDivisionError:
                percent = 0
        print('Total Issues: {}, #Issues Done: {}, %Completion: {}'.format(cntIssueTotal, cntIssueDone, percent))
    try:
        percent = round(float(cntEpicDone/cntEpicTotal)*100,2);
    except ZeroDivisionError:
        percent = 0
    print('\n----- Total Epics: {}, #Epics Done: {}, %Completion: {} ----'.format(cntEpicTotal, cntEpicDone, percent))
    print('\nSummary report generated successfully.')
#print("\nCount of issues from this JQL: ", len(epicList), '\n')

# for epic in epicList:
#     print('ID: {}, Summary: {}'.format(epic.key, epic.fields.summary))
#     print("Status: ", epic.fields.status.name)  #status
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
