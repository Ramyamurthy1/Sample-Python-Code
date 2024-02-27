###############################################################
# scan the gitlab project and read vulberability report. 
# create a JIRA defect if the vulnerability does not exist
################################################################


import json
from jira import JIRA
import requests
from duplicate_jira import duplicate_jira
#from Jira_vulnerability.auth import auth

def read_vulnerability_report():
    # Path to the JSON file
    file_name="x.json"
    
    user=''    
    apassword=''
    project="project_key"
    
    auth = requests.auth.HTTPBasicAuth(user, apassword)
    jira_url="https://jira.com.xx.xx"
    headers = {"Content-Type": "application/json"}

    # Read the JSON file
    try:
        with open(file_name) as file:
            data = json.load(file)
    except Exception as e:
        print(f"Failed to read the file: {e}")
    
    # Print the value of element0
    for i in range(0, len(data)):
        print(len(data ))
        print("i ==", i)
        id=str(data[i]["id"])
        severity=data[i]["severity"]
        description=data[i]["description"]
        summary=str(data[i]["name"])        
        team={"value": "DevSecOps"}
        jira_severity={"value": "Critical"}
        
        #print(f"summary before: {summary}")

        # Read summary till '(' is encountered. JQL Query is throwing error when '(' is encountered. Hence reading summary only till ( is encountered
        summary = summary.split('(')[0].strip()

        print(f"ID: {id}")
        print(f"Severity: {severity}")
        print(f"summary: {summary}")
        
        
    
    #check if the JIRA defect with same vulnerability exists    
        issues=duplicate_jira(project, summary)
        #print(issues)
        #print(len(issues))
        if len(issues) > 0:
            print(f"Jira issue with summary {summary} exists. Not creating new defect")
        else:
            print(f"Creating new Jira issue for {summary}")
            #create_jira_issue(jira_handle, project, summary, description, severity, team, jira_severity)
            
  

            jira_payload={
                "fields": {
                    "project": {"key": project},
                    "summary": summary,
                    "description": "Found vulnerability " + id + " in file " + description + ". Severity: " + severity,
                    "issuetype": {"name": "Bug"},
                    "customfield_10207": jira_severity,
                    "customfield_10200": team,
                    "customfield_11110": {"value": "Security"},
                    "customfield_10500": [{"value":"NFT"}]
                    
                    
                }
            }

            print(jira_payload)
            try:
                response = requests.post(
                    f"{jira_url}/rest/api/2/issue",
                    headers=headers,
                    auth=auth,
                    data=json.dumps(jira_payload)
                )
            except Exception as e:
                print(f"Failed to create Jira issue: {e}")

            print(response.status_code)
            print(response.text)



result=read_vulnerability_report()
print(result)


