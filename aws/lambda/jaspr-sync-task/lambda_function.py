import json
import boto3
from decimal import Decimal
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    # check if data is in json format
    try:
        if type(event) is str:
            data = json.loads(event)
        else:
            data = event
    except ValueError:
        return return_error(400, 'bad data sent')

    # init needed dynamodb access and table
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('jaspr-tasks')
    except Exception as e:
        return return_error(500, 'arjun did a stupid', e)

    # iterate through all sync items sent and put new ones in db
    for t in list(data):
        for key, value in t.items():
            if type(value) is float:
                t[key] = int(value)
        try:
            table.put_item(
                Item=t,
                ConditionExpression='attribute_not_exists(#u) OR #m < :m',
                ExpressionAttributeValues={
                    ':m' : t['modified']
                },
                ExpressionAttributeNames={
                    '#u': 'uuid',
                    '#m': 'modified'
                }
            )
        except ClientError as e:
            print(e)
        except Exception as e:
            return return_error(500, 'put in db failure', e)
    # scan db to get all items
    try:
        response = table.scan(
            ConsistentRead=True
        )
    except Exception as e:
        return return_error(500, 'scan db failure', e)

    task_list = response['Items']

    # return scanned items
    return {
        'statusCode': 200,
        'body': task_list
    }

def return_error(code, msg, body={}):
    return {
        'statusCode': code,
        'message': msg,
        'body': body
    }
