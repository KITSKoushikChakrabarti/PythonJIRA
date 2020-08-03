# Developed by Koushik - Apr 2020
# Purpose: Gets JIRA Issue details as RAW JSON
from jira import JIRA
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
    print("Rawdata:--------------------------\n", issue.raw)
    print("\n-----------------------------------")
print("Exiting program...")

# Once you get the RAW JSON, view it in http://jsonviewer.stack.hu/ to get detailed fields and values.
