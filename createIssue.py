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

######## Updating an Issue ######
# Get an issue.
issue = jira.issue("JRA-1330")

# Change the issue's summary and description.
issue.update(summary="I'm different!", description="Changed the summary to be different.")

# Change the issue without sending updates
issue.update(notify=False, description="Quiet summary update.")

# You can update the entire labels field like this
issue.update(fields={"labels": ["AAA", "BBB"]})

# Or modify the List of existing labels. The new label is unicode with no
# spaces
issue.fields.labels.append(u"new_text")
issue.update(fields={"labels": issue.fields.labels})

# Send the issue away for good.
issue.delete()

# Linking a remote jira issue (needs applinks to be configured to work)
issue = jira.issue("JRA-1330")
issue2 = jira.issue("XX-23")  # could also be another instance
jira.add_remote_link(issue, issue2)