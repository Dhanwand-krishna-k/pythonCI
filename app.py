import json

import requests

print("Function is starting....")

def lambda_handler(event, context):
    
    print("The message from api",event.get("body"))

    try:
        data = requests.get("https://lf5g3m9z21.execute-api.ap-south-1.amazonaws.com/dev/hello", timeout=2)
    except requests.RequestException as e:
         # Send some context about this error to Lambda Logs
        print(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
             "data": data.text.replace("\n", "")
        }),
    }
