import json
import boto3
from decimal import Decimal
from uuid import UUID
import datetime
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    
   #check if uuid is sent in event and formatted correctly 
    try:
        if type(event) is dict:
            data=event
        else:
            data=json.loads(event)
        UUID(data['uuid'])
    except ValueError: 
        return(return_error(400, 'bad uuid'))
    
    
    #init needed dynamodb access and table
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('eve-tasks')
    except: 
        return(return_error(500, 'arjun did a stupid'))
    
    #get current date in isoformat
    cur_date = str(datetime.datetime.utcnow().replace(microsecond=0).isoformat())
    cur_date = cur_date.replace('-','')
    cur_date = cur_date.replace(':','')
    cur_date += 'Z'
    
    #get old item from db
    try:
        response = table.get_item(
            Key = {
            'uuid' : data['uuid']
            }     
        )
    except ClientError as e: 
        return(return_error(500, 'failure to retrieve old task',e))
    else:
        if 'Item' not in response:
            return(return_error(400, 'task not in database'))
        else:
            task = response['Item']
    
    #update item with fields
    task['modified']=cur_date
    for key,value in data.items():
        task[key]=value
    
    try:
        response = table.put_item(
            Item=task
        )
    except Exception as e: 
        return(return_error(500, 'failure to put task into db',e))
    
    
    #return good
    return {
        'statusCode': 200,
        'body': task
    }

def return_error(code , msg, body={}):
    return {
        'statusCode': code,
        'message': msg,
        'body': body
    }
