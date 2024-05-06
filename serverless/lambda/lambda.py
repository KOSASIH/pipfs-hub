import json

def lambda_handler(event, context):
    """AWS Lambda function handler."""
    print(json.dumps(event, indent=2))
    return {
       'statusCode': 200,
        'body': json.dumps('Hello, World!')
    }
