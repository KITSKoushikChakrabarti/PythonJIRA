
# Developed by Koushik - Sep 2020
# Purpose: Create JIRA Hierarchy Summary report - version 4
# Get a hierarchical summary view of JIRA issues (initiatives--> Deliverables --> Epics -->Stories)  (HTML reporting)
from jira import JIRA
from datetime import datetime
from os import path
import os
import getpass

# login to JIRA using username and password
print("----- This python program will display a 2-level Hierarchical Summary from JIRA as HTML Report ----- ")
print("\nEnter credentials to login to JIRA:")
user = input("Username: ")
pw = getpass.getpass()
jira = JIRA(auth=(user, pw), options={'server': 'https://jira.kfplc.com'})

# Enter a JQL query to generate the output resultset which will be the source of issues to be cloned  
issueID = input("\nEnter a JIRA ID (type 0 to exit): ")
jqlDemand = '"Parent Link"=' + issueID;

# Get initial details of the JIRA id
issue = jira.issue(issueID) 

# Create Reports folder if not existing
filepath = os.getcwd() + "\\Reports"
if(path.exists(filepath) == False):
   os.mkdir(filepath)
   print("Reports folder created %s" % filepath)   

# Display issue Details in HTML table
# If File doesn't exist, it will create automatically using JIRA id and DateTime
# filename = 'C:\\PERSONAL\\' + 'JIRASummaryReport.html'
now = datetime.now()
dt = now.strftime("%d-%m-%Y")
filename = filepath + "\\"+ issueID + ' SummaryReport ' + dt + '.html'
print("Report File = ", filename)
html_file= open(filename,"w")
html_str = """
<head>
<style type="text/css">
p {
  color: #FFFF88;
}
table {
  border-collapse: separate;
  border-spacing: 0;
  color: #888888;
  font: 14px/1.4 "Helvetica Neue", Helvetica, Arial, sans-serif;
}
caption, th, td {
  padding: .2em .8em;
  border: 1px solid #fff;
}

caption {
  background: #FFF1D8;
  font-weight: bold;
  font-color: #000000;
  font-size: 1.1em;
}
th {
  background-color: #00FFA5;
}
th,
td {
  padding: 3px 3px;
  vertical-align: middle;
  }
th:first-child {
  text-align: left;
}
tbody tr:nth-child(even) {
  background: #f0f0f2;
}
td {
  border-bottom: 1px solid #cecfd5;
  border-right: 1px solid #cecfd5;
}
td:first-child {
  border-left: 1px solid #cecfd5;
}
tfoot {
  text-align: right;
}
tfoot tr:last-child {
  background: #f0f0f2;
}
</style>
</head>
<body>
<table style="width:50%" border="1px" bordercolor="000000" align="center" >
  <caption> JIRA Summary Report </caption>
  <tr>
    <th style="width:20%">Properties</th>
    <th style="width:80%">Values</th>
  </tr>
  """  
html_str += "<tr><td>ID</td><td><a href='https://jira.kfplc.com/browse/" + issue.key + "'>" + issue.key + "</a></td></tr>"
html_str += "<tr><td>Project</td><td>" + issue.fields.project.key + "</td></tr>"
html_str += "<tr><td>Issue Type</td><td>" + issue.fields.issuetype.name + "</td></tr>"
html_str += "<tr><td>Summary</td><td>" + issue.fields.summary + "</td></tr>"
html_str += "<tr><td>Description</td><td>" + issue.fields.description + "</td></tr>"
html_str += "<tr><td>Status</td><td>" + issue.fields.status.name + "</td></tr>"
# html_str += "<tr><td>Priority</td><td>" + issue.fields.priority.name + "</td></tr>"

html_str += "</table>"

html_str += """
<BR><BR><table style="width:80%" border="1px" bordercolor="000000" align="center">
  <caption> Summary of Child issues </caption>
  <tr>
    <th style="width:10%">ID</th>
    <th style="width:10%">Type</th>
    <th style="width:40%">Title</th>
    <th style="width:10%">Status</th>
    <th style="width:10%">Total Issues</th>
    <th style="width:10%"># Issues Done</th>
    <th style="width:10%; background-color:#99CFE0;">% Complete</th>    
  </tr>
  """
# use this code to get more than 50 results in search issues in an interative loop
block_size = 200
block_num = 0
cntEpicDone = 0
cntEpicTotal = 0
cntIssueTotal = 0
cntIssueDone = 0
jqlSortOrder = ' ORDER BY Key ASC'    
while issueID != '0':        
    start_idx = block_num*block_size
    epicList = jira.search_issues(jqlDemand + jqlSortOrder, start_idx, block_size)    
    cntEpicTotal = len(epicList) # save the Epic Total for display
    if len(epicList) == 0:
        # Retrieve issues until there are no more to come
        break    
    # print("\nCount of Epics in this demand: ", len(epicList), '\n')            
    block_num += 1
    for epic in epicList:
        # print('ID: {}, Summary: {}'.format(epic.key, epic.fields.summary))
        # print("Status: ", epic.fields.status.name)  #status
        print('Child Issue: {}'.format(epic.key))        
        jqlEpic = '"Parent Link"=' + epic.key         
        if(epic.fields.status.name == "Done"):
            cntEpicDone += 1 # save the epic done count for display
        
        html_str += "<tr><td><a href='https://jira.kfplc.com/browse/" + epic.key + "'>" + epic.key + "</a></td>"
        html_str += "<td>" + epic.fields.issuetype.name + "</td>"
        html_str += "<td>" + epic.fields.summary + "</td>"
        html_str += "<td>" + epic.fields.status.name + "</td>"
        
        issueList = jira.search_issues(jqlEpic + jqlSortOrder, 0, block_size)
        issueDoneList = jira.search_issues(jqlEpic + ' AND status = Done' + jqlSortOrder, 0, block_size)
        
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
        print('--Total Issues: {}, #Issues Done: {}, %Completion: {}%'.format(cntIssueTotal, cntIssueDone, percent))

        html_str += "<td>" + str(cntIssueTotal) + "</td>"
        html_str += "<td>" + str(cntIssueDone) + "</td>"
        html_str += "<td><b>" + str(percent) + "</b></td></tr>"
    try:
        percent = round(float(cntEpicDone/cntEpicTotal)*100,2);
    except ZeroDivisionError:
        percent = 0
    print('\n----- Total Child Issues: {}, #Child Issues Done: {}, %Completion: {}% ----'.format(cntEpicTotal, cntEpicDone, percent))
    print('\nSummary report generated successfully.')

    html_str += "</table>" # completion of previous table HTML
    html_str += """<BR><BR><table style="width:60%" border="2px" bordercolor="000000" align="center">
    <caption> Overall Completion Status of the Issue </caption>
    <tr>
        <th style="width:30%">Number of Child Issues Done</th>
        <th style="width:30%">Total number of Child Issues</th>
        <th style="width:60%; background-color:#99CFE0;">Overall % Complete</th>    
    </tr>
    """
    html_str += "<td align='center'><H1>" + str(cntEpicDone) + "</H1></td>"
    html_str += "<td align='center'><H1>" + str(cntEpicTotal) + "</H1></td>"
    html_str += "<td align='center'><H1>" + str(percent) + "</H1></td></tr></table>"

    html_str += "<BR><BR>"
    html_str += "</body>"
    html_file.write(html_str)
    html_file.close()
