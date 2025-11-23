import os
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.getenv('TABLE_NAME')
table = dynamodb.Table(table_name)

def main(event, context):
    print("Event:", json.dumps(event))
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        table.put_item(Item={
            'id': key,
            'bucket': bucket
        })
    return {"statusCode": 200}
