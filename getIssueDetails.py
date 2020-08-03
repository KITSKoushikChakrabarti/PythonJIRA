# Developed by Koushik - Apr 2020
# Purpose: Gets detailed attributes about a JIRA issue
from jira import JIRA
import re  # use of regular expression in Python
import getpass

# login to JIRA using username and password
print("Enter credentials to login to JIRA:")
user = input("Username: ")
pw = getpass.getpass()
jira = JIRA(auth=(user, pw), options={'server': 'https://jira.kfplc.com'})

issueID = ""
# get an issue details by prompting the JIRA id
while issueID != '0':
    issueID = input("Enter JIRA id (type 0 to exit): ")
    if issueID == '0':
        break
    issue = jira.issue(issueID)

    print("-----------------------------------")
    print('id: ', issue.key)  # DRRR-437 JIRA id
    print("Project: ", issue.fields.project.key)  #DRRR
    print("IssueType: ", issue.fields.issuetype.name)  #story
    print("Reporter: ", issue.fields.reporter.displayName)  #creator
    print("Summary: ", issue.fields.summary)  #title of issue
    print("Description: ", issue.fields.description)  #title of issue
    print("Status: ", issue.fields.status.name)  #status
    #print (issue.fields.project.id) #project id 17508
    print("Assignee: ", issue.fields.assignee)  #assignee
    print("Priority: ", issue.fields.priority.name)  #priority
    print("Labels: ", ' '.join(issue.fields.labels))  #print list of labels

    # custom fields
    #print(issue.fields.customfield_10000) #None
    #print(issue.fields.customfield_10001) #None
    print("Story Point: ",
          int(issue.fields.customfield_10002))  # Story Point as 1.0 or 2.0
    #print(issue.fields.customfield_10003)  #None
    #print(issue.fields.customfield_10004) #9223372036854775807
    #sprintObj = issue.fields.customfield_10005
    #print(sprintObj)
    sprint_name = re.findall(r"name=[^,]*",
                             str(issue.fields.customfield_10005[0]))
    print("Sprint: ", str(sprint_name))  # sprint name
    print("Epic: ", str(issue.fields.customfield_10006))  # Epic value DRRR-174
#    print("Rawdata: ", issue.raw)
    print("-----------------------------------")
    #print(str(issue.fields.customfield_10007))
    #print(str(issue.fields.customfield_10008))
    #print(str(issue.fields.customfield_10009))
    #print(str(issue.fields.customfield_10010))
    #print(str(issue.fields.customfield_10011))
    #print(str(issue.fields.customfield_10012))
    #print(str(issue.fields.customfield_10013))
    #print(str(issue.fields.customfield_10014))
    #print(str(issue.fields.customfield_10015))
    #print(str(issue.fields.customfield_10016))
    #print (issue.fields.timetracking.originalEstimate)

print("Exiting program...")
