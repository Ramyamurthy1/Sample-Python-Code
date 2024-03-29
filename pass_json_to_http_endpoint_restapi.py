#############################################################
#
#   Script to pass entire json file to an REST Endpoint
#
#
#############################################################


import json
from get_token import get_token
import requests
import os
from datetime import datetime



NSD_ENDPOINT_URL='https://sampleurl.com:80/xxx/yyy'
NST_ENDPOINT_URL='https://sampleurl.com:80/xxx/yyy'
CNSST_ENDPOINT_URL='https://sampleurl.com:80/xxx/yyy'

def deploy_slice_template(query_json, SP_ENDPOINT):
  print("inside slice template")
  #print("query_json =", query_json)
  try:
    headers={"content-type": "application/json", "Authorization":get_token()}
    provide_request=requests.post(SP_ENDPOINT,headers=headers,json=query_json,verify=False)

    print("*******", provide_request)
  except Exception as e:
    print("e", e)

  http_response=provide_request.status_code
  print(http_response)
  reason=provide_request.json()
  print(reason)


list_file=os.listdir("templates")
for i in list_file:
    BASE_DIR="templates"
    filename=os.path.join(BASE_DIR,i)
    print(f'{datetime.now()}  : Pushing Template {filename}')
    with open(filename) as json_object:
        i = json.load(json_object)
        if "nsd" in filename:
            deploy_slice_template(i, NSD_ENDPOINT_URL)
        elif "nst" in filename:
            deploy_slice_template(i, NST_ENDPOINT_URL)
        elif "cnsst" in filename:
            deploy_slice_template(i, CNSST_ENDPOINT_URL)
