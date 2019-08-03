import json
import subprocess
import requests
from datetime import datetime
import re

sync_endpoint='https://api.arjungandhi.com/jaspr/task/sync'
task_warrior_time_format='%Y%m%dT%H%M%SZ'

#run task export and get result
result = subprocess.getoutput(['task export'])
task_list=json.loads(result)

#delete all tasks that are deleted
task_list=[t for t in task_list if t['status'] != 'deleted']

#go through tasks and change time to millis
for task in task_list:
    #go through each task list time and convert check if it is a date if it is convert to millis
    for key,value in task.items():
        #convert all string time to millis since epoch
        if type(value) is str and re.fullmatch('[0-9]{8}T[0-9]{6}Z',value):
            value=datetime.strptime(value ,task_warrior_time_format).timestamp()*1000
        #convert all floats to ints
        if type(value) is float:
            task[key]=int(value)


#take task_list and make request to sync
r = requests.post(url = "https://api.arjungandhi.com/jaspr/task/sync", data = json.dumps(task_list))
#task list is body of request
print(r.json())
if r.status != 200:
    raise Exception(f'Server did not responded with {r.status}')

task_list=r.json
#go through tasks and change time to millis
for task in task_list:
    #go through each task list time and convert check if it is a date if it is convert to millis
    for key,value in task.items():
        #convert all string time to millis since epoch
        if type(value) is float and value>1000000:
            value=datetime.strptime(value ,task_warrior_time_format).timestamp()*1000
        #convert all floats to ints
        if type(value) is float:
            task[key]=int(value)
