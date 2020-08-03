from jira import JIRA
import getpass
 
pw = getpass.getpass()
jira = JIRA(auth=('chakrk03', pw) , options = {'server': 'https://jira.kfplc.com'})

# Linking a remote jira issue (needs applinks to be configured to work)
issue = jira.issue("DRRR-437")
issue2 = jira.issue("DRRR-484")
jira.add_remote_link(issue, issue2)
