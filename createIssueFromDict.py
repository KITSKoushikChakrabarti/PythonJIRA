# Developed by Koushik - Apr 2020
# Purpose: Create a JIRA issue using dictionary
from jira import JIRA
import getpass

# login to JIRA using username and password
print("Enter credentials to login to JIRA:")
user = input("Username: ")
pw = getpass.getpass()
jira = JIRA(auth=(user, pw), options={'server': 'https://jira.kfplc.com'})

# ---- Create JIRA issue using dictionary
jira_dict_convert = {
  'project': {'key': 'DRRR'},  
  'summary': 'Test Bug title using Dictionary - JIRA Python',  
  'issuetype': {'name': 'Bug'},
  'priority': {'name': 'High'},
  'description':  'Test story description using Dict - JIRA Python'
}
newID = jira.create_issue(jira_dict_convert)
print('\nNew issue created using dictionary: ', newID)


    