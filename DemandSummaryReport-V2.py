
# Developed by Koushik - Sep 2020
# Purpose: Create Demand/Initiative summary report - version 2 (improve performance)

from jira import JIRA
import getpass

# login to JIRA using username and password
print("----- This python program will display a Demand/Initiative Summary from JIRA as console output ----- ")
print("\nEnter credentials to login to JIRA:")
user = input("Username: ")
pw = getpass.getpass()
jira = JIRA(auth=(user, pw), options={'server': 'https://jira.kfplc.com'})

# Enter a JQL query to generate the output resultset which will be the source of issues to be cloned  
jql = input("\nEnter an Initiative or Demand ID (e.g. DEM-489): ")
jqlDemand = '"Parent Link"=' + jql;

# run the JQL to get child issues (Epics) resultset for that Demand
#epicList = jira.search_issues(jqlDemand) 

# use this code to get more than 50 results in search issues in an interative loop
block_size = 200
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
        
        issueList = jira.search_issues(jqlEpic, 0, block_size)
        issueDoneList = jira.search_issues(jqlEpic + ' AND status = Done', 0, block_size)
        
        cntIssueTotal = len(issueList) # save the Issue Total for display        
        cntIssueDone = len(issueDoneList) # save the Issue Done for display        
        # for issue in issueList:            
        #     if(issue.fields.status.name == "Done"):
        #         cntIssueDone += 1 # save the issue done count for display
            # print('Issue: {}'.format(issue.key)) 
        try:
            percent = round(float(cntIssueDone/cntIssueTotal)*100,2);
        except ZeroDivisionError:
            percent = 0
        print('Total Issues: {}, #Issues Done: {}, %Completion: {}%'.format(cntIssueTotal, cntIssueDone, percent))
    try:
        percent = round(float(cntEpicDone/cntEpicTotal)*100,2);
    except ZeroDivisionError:
        percent = 0
    print('\n----- Total Epics: {}, #Epics Done: {}, %Completion: {}% ----'.format(cntEpicTotal, cntEpicDone, percent))
    print('\nSummary report generated successfully.')
