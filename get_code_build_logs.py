##########################################################################################################################################
##########################################################################################################################################

###   This python code will fetch logs for commit. Developer commits his/her code into code commit and the codee pipeline is triggered. ##
###   This code will help fetch the codebuild logs for this commit.     
##    uses AWS's boto3 SDK

##########################################################################################################################################
##########################################################################################################################################

import boto3
import botocore
import time
import pprint

client = boto3.client('codecommit')

filename="hello.sh" ####Sample file with some text such as "hello"
f=open("hello.sh", "r")
data=f.read()
print(data)

#get the code commit ID
response=client.get_branch(
    repositoryName='Test-Cloudwatch',
    branchName='main'
)

print(response)

parentCommitId=response["branch"]["commitId"]
print(parentCommitId)
response = client.put_file(
    repositoryName='Test-Cloudwatch',
    branchName='main',
    fileContent=data,
    filePath=filename,
    fileMode='EXECUTABLE',
    parentCommitId=parentCommitId,
    commitMessage='test',
    name='ramya',
    email='ramya'
)
print(response)

commitId=response["commitId"]
print(commitId)




#get code build id


code_build_client = boto3.client('codebuild')

code_build_response = code_build_client.list_builds_for_project(
    projectName='Test-build-cloud-watch',
    sortOrder='DESCENDING'
    )
id=code_build_response["ids"][0]
print("id ==", id)
new_id=id[id.rfind(':'):].strip(':')
print("new id ==", new_id)

time.sleep(15)


# get cloudwatch logs

cloudWatchLogclient = boto3.client('logs')

latestlogStreamName=commitId
cloudwatch_time=100000
currentSystemTime=current_milli_time()
executionTime=currentSystemTime+cloudwatch_time
attempts = 0
max_attempts = 10
cloud_watch_client=None

cloudWatchResponse = cloudWatchLogclient.get_log_events(
            logGroupName="/aws/codebuild/Test-build-cloud-watch", # Can be dynamic
            logStreamName=new_id,
)
cloudWatchResponse=pprint.pformat(cloudWatchResponse)

