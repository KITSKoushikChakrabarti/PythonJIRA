# Developed by Koushik - Apr 2020
# Purpose: Create a JIRA issue
from jira import JIRA
import getpass

# login to JIRA using username and password
print("Enter credentials to login to JIRA:")
user = input("Username: ")
pw = getpass.getpass()
jira = JIRA(auth=(user, pw), options={'server': 'https://jira.kfplc.com'})

# ---- Create JIRA issue by passing values
new_issue = jira.create_issue(project='DRRR', summary="Test story title from JIRA-Python automation script",  description="Test story description from JIRA Python automation script", issuetype={'name': 'Story'}, priority={'name': 'High'})
print('\nNew issue created: ', new_issue)

