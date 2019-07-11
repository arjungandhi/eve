import json
import boto3
from decimal import Decimal
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    # check if data is in json format
    try:
        if type(event) is dict:
            data = event
        else:
            data = json.loads(event)
    except ValueError:
        return return_error(400, 'bad data sent')

    # init needed dynamodb access and table
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('jaspr-tasks')
    except Exception as e:
        return return_error(500, 'arjun did a stupid', e)

    # iterate through all sync items sent and put new ones in db
    for t in data:
        for key, value in t:
            if type(value) is float:
                t[key] = Decimal(key)
        try:
            table.putItem(
                Item=t,
                ConditionalExpression='attribute_not_exists uuid OR #m < :m',
                ExpressionAttributeValues={
                    ':m': t['modified'],
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
            ConsistentRead=True,
            FilterExpression='status != :s',
            ExpressionAttributeValues={
                ":s": "deleted"
            }
        )
    except Exception as e:
        return return_error(500, 'scan db failure', e)

    task_list = response['Items']

    # return scanned items
    return {
        'statusCode': 200,
        'body': task_list
    }


FilterExpression


def return_error(code, msg, body={}):
    return {
        'statusCode': code,
        'message': msg,
        'body': body
    }
