from kubernetes import config
from kubernetes.client import Configuration
from kubernetes.client.api import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream
import sys
import datetime
import time
from datetime import datetime
from datetime import date
from time import strftime
from time import sleep

print(f'{datetime.now()}  : "Executing Invoking Test Automation from the pod')


config.load_kube_config()
namespace = "ubuntu"

config.load_kube_config()
  
try:
            c = Configuration().get_default_copy()
except AttributeError:
            c = Configuration()
            c.assert_hostname = False
Configuration.set_default(c)
core_v1 = core_v1_api.CoreV1Api()
    
pod_list=core_v1.list_namespaced_pod(namespace)
    
try:
      for pod in pod_list.items:
         pod_name=pod.metadata.name
      print(f'{datetime.now()}  : Following pods Exist {pod_name}')
except ValueError as esc:
      print(f'{datetime.now()}  : No ALD pods exist')
      sys.exit(2)


TestDataSheet=sys.argv[1]
print(f'{datetime.now()}  : "The Test sheet to be executed is {TestDataSheet}')


#exec_cd_command = ["/bin/sh","-c", "cd /cicd/TestAutomation/Code/all_rfss/"]
#resp_cd = stream(core_v1.connect_get_namespaced_pod_exec, pod_name, namespace, command=exec_command, stderr=True, stdin=False, stdout=True, tty=False)

exec_command = ["/bin/sh","-c", "python3 /cicd/TestAutomation/Code/all_rfss/main_csv.py "+" "+"/cicd/TestAutomation/Code/all_rfss/"+TestDataSheet]
#exec_command = ["/bin/sh","-c", "python3 /cicd/TestAutomation/Code/all_rfss/main_csv.py "+" "+"/cicd/TestAutomation/Code/all_rfss/"+TestDataSheet]
print(f'{datetime.now()}  : Exec command is  {exec_command}')
resp = stream(core_v1.connect_get_namespaced_pod_exec, pod_name, namespace, command=exec_command, stderr=True, stdin=False, stdout=True, tty=False)

print(f'{datetime.now()}  : resp is {resp}')


exec_ls_command = ["/bin/sh","-c", "ls -alrt /root"]
resp_ls = stream(core_v1.connect_get_namespaced_pod_exec, pod_name, namespace, command=exec_ls_command, stderr=True, stdin=False, stdout=True, tty=False)
print(f'{datetime.now()}  : resp _ls is {resp_ls}')



exec_copy_command = ["/bin/sh","-c", "mv *.csv /results"]
resp_ls = stream(core_v1.connect_get_namespaced_pod_exec, pod_name, namespace, command=exec_copy_command, stderr=True, stdin=False, stdout=True, tty=False)
print(f'{datetime.now()}  : resp _ls is {resp_ls}')

exec_copy_command = ["/bin/sh","-c", "mv *.log /logs"]
resp_ls = stream(core_v1.connect_get_namespaced_pod_exec, pod_name, namespace, command=exec_copy_command, stderr=True, stdin=False, stdout=True, tty=False)
print(f'{datetime.now()}  : resp _ls is {resp_ls}')

exec_copy_command = ["/bin/sh","-c", "mv *.json /jsons"]
resp_ls = stream(core_v1.connect_get_namespaced_pod_exec, pod_name, namespace, command=exec_copy_command, stderr=True, stdin=False, stdout=True, tty=False)
print(f'{datetime.now()}  : resp _ls is {resp_ls}')



try:
  exec_cp_json_command = ["/bin/sh","-c", 'aws s3 cp /results s3://rfs-test-results/Test-Results/results --recursive --exclude "*" --include "*csv" ']
  resp_cp_json = stream(core_v1.connect_get_namespaced_pod_exec, pod_name, namespace, command=exec_cp_json_command, stderr=True, stdin=False, stdout=True, tty=False)
  print(f'{datetime.now()}  : resp _ls is {resp_cp_json}')
except ValueError as esc:
  print(f'{datetime.now()}  : Could Not COPY JSON FILES')


try:
  exec_cp_json_command = ["/bin/sh","-c", 'aws s3 cp /logs s3://rfs-test-results/Test-Results/logs --recursive --exclude "*" --include "*log" ']
  resp_cp_json = stream(core_v1.connect_get_namespaced_pod_exec, pod_name, namespace, command=exec_cp_json_command, stderr=True, stdin=False, stdout=True, tty=False)
  print(f'{datetime.now()}  : resp _ls is {resp_cp_json}')
except ValueError as esc:
  print(f'{datetime.now()}  : Could Not COPY JSON FILES')



try:
  exec_cp_json_command = ["/bin/sh","-c", 'aws s3 cp /jsons s3://rfs-test-results/Test-Results/jsons --recursive --exclude "*" --include "*json" ']
  resp_cp_json = stream(core_v1.connect_get_namespaced_pod_exec, pod_name, namespace, command=exec_cp_json_command, stderr=True, stdin=False, stdout=True, tty=False)
  print(f'{datetime.now()}  : resp _ls is {resp_cp_json}')
except ValueError as esc:
  print(f'{datetime.now()}  : Could Not COPY JSON FILES')



'''
with TemporaryFile() as tar_buffer:
  exec_stream = stream(core_v1.connect_get_namespaced_pod_exec, pod_name, namespace, command=exec_cp_command, stderr=True, stdin=False, stdout=True, tty=False)
  try:  
        while exec_stream.is_open():
            exec_stream.update(timeout=1)
            if exec_stream.peek_stdout():
                out = exec_stream.read_stdout()
                tar_buffer.write(out.encode('utf-8'))
            if exec_stream.peek_stderr():
                logger.debug("STDERR: %s" % exec_stream.read_stderr())
        exec_stream.close()
        tar_buffer.flush()
        tar_buffer.seek(0)
        with tarfile.open(fileobj=tar_buffer, mode='r:') as tar:
            member = tar.getmember(source_path)
            tar.makefile(member, destination_path)
            return True
  except Exception as e:
        raise manage_kubernetes_exception(e)
'''        
