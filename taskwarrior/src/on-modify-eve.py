#!/usr/bin/env python

import sys
import json

#gets task
added_task = json.loads(sys.stdin.readline())
modified_task = json.loads(sys.stdin.readline())

#do stuff with added task
file=open('/home/arjun/workspace/eve/taskwarrior/test/onadd.txt','a')
file.write(json.dumps(added_task))
file.write(json.dumps(modified_task))
file.close()



#exits added task correctly
print(json.dumps(modified_task))
sys.exit(0)
