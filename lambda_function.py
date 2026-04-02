import json

print('Loading function')

def lambda_handler(event, context):
    
    return {
        
        "statusCode": 200,
        "body": {
            "message":"version 4",
            "type":"test2"
        },
        
    }
