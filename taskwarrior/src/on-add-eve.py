#!/usr/bin/env python

import sys
import json

#gets task
task = json.loads(sys.stdin.readline())


#do stuff with added task
file=open('/home/arjun/workspace/eve/taskwarrior/test/onadd.txt','a')
file.write(json.dumps(task))
file.close()



#exits added task correctly
print(json.dumps(task))
sys.exit(0)
