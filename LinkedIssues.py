from jira import JIRA
import getpass
 
pw = getpass.getpass()
jira = JIRA(auth=('chakrk03', pw) , options = {'server': 'https://jira.kfplc.com'})

# Linking a remote jira issue (needs applinks to be configured to work)
issue = jira.issue("FDE-154")

# parent_issue = 'FDE-176'
# jira.add_remote_link(new_issue, parent_issue) ### not working

# You can update the entire labels field like this
issue.update(fields={"Parent Link": "ED-8"})

# print("Epic: ", str(issue.fields.customfield_10006))  # Epic value DRRR-174
# Or modify the List of existing labels. The new label is unicode with no
# spaces
# issue.fields.labels.append(u"new_text")
# issue.update(fields={"labels": issue.fields.labels})

# new_issue = 'FDE-175'
# parent_issue = 'FDE-176'

# ######### FDE-175 Duplicates FDE-176
# jira.create_issue_link(
#     type="Duplicate",
#     inwardIssue=new_issue,
#     outwardIssue=parent_issue,
#     comment={
#         "body": "Linking '%s' --&gt; '%s'" % (new_issue, parent_issue),
#     }
# )