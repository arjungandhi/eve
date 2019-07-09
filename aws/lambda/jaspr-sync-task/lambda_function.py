import json
import boto3
from decimal import Decimal
from uuid import UUID
import datetime
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    
   #check if data is in json format
    try:
        if type(event) is dict:
            data=event
        else:
            data=json.loads(event)
    except ValueError: 
        return(return_error(400, 'bad data sent'))
    
    
    #init needed dynamodb access and table
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('eve-tasks')
    except: 
        return(return_error(500, 'arjun did a stupid'))
    
    #get current date
    cur_date = str(datetime.datetime.utcnow().replace(microsecond=0).isoformat())
    cur_date = cur_date.replace('-','')
    cur_date = cur_date.replace(':','')
    cur_date += 'Z'
    
    #iterate through all sync items sent
    for t in data:
        #check if task in db or sent task is newer
        try:
        response=table.get_item(
        Key={
            'uuid' : t['uuid']
        },
        ProjectionExpression='modified'
        )
        except ClientError as e:
            return(return_error(500,'task db not working right'))
        
        #convert all floats to decimal cause dynamos a pain in the ass
        for key,value in t 
            if type(value) is float:
                t[key]=Decimal(value)
        
        #if task date is bigger than dynamodb task then add it or if its not in dynamo also add it 
        if 'Item' in response:
            db_task=response['Item']
            
    
    
def translate_date(string_date):
    return datetime.datetime.strptime(string_date,'%Y%m%dT%H%M%SZ')
    

def return_error(code , msg, body={}):
    return {
        'statusCode': code,
        'message': msg,
        'body': body
    }
