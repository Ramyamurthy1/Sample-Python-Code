########################################################
########################################################
## If you need to use the logging function with custome formatter then the sample code is below:
## For example, you might want to log the logs to kibana in specific format.
## Different handlers can be added for stdout or syslog
## 


import logging
import sys
from datetime import datetime


request_id="7678678"
timestamp = datetime.now().isoformat()
extra= {
            "@timestamp": timestamp,
            "@version": "1",
            #"message": message,
            "external_request_id": str(request_id)
        }
#extra = {'app_name':request_id}

logger = logging.getLogger(__name__)
syslog = logging.StreamHandler(sys.stdout)
#formatter = logging.Formatter('%(asctime)s %(app_name)s : %(message)s')
#formatter = logging.Formatter('[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s')
formatter = logging.Formatter('%(@timestamp)s : %(@version)s : %(external_request_id)s :  %(levelname)s -  %(message)s')
syslog.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(syslog)

logger = logging.LoggerAdapter(logger, extra)
logger.info('The sky is so blue')
logger.error("hey! i got error")



