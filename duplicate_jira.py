################################################################################
##  Check if duplicate JIRA defect exists for a summary in vulnerability report
################################################################################

from jira import JIRA

def duplicate_jira(project, summary):

# Replace with your Jira server URL and credentials
      jira_server = "https://jira.com"

      #Set your Jira credentials
      user=''    
      apassword=''
      

      options = {'server': jira_server }
      jira_handle = JIRA(options, auth=(user, apassword))
      project = jira_handle.project('project_key')
      #search_string="quartz-jobs 2.3.2 a"
      search_string = summary

      project_id = project.id
      jql_query = f"project = {project_id} AND Summary ~ '{summary}'"
      print("^^^^^^^^^^^^^^^^^")      
      print(f"jql_query = {jql_query}")
     
      # Search for issues
      issues = jira_handle.search_issues(jql_query)
      print("**********")
      #print(issues)
      return issues
