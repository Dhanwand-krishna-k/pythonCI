import json
import lambda_function  # Assuming your Lambda code is in app.py

def test_lambda_handler_success():
    # 1. Arrange: Create a fake event and context
    event = {"key": "value"}
    context = {}

    # 2. Act: Call the function
    response = lambda_function.lambda_handler(event, context)

    # 3. Assert: Check the JSON structure and status code
    assert response['statusCode'] == 200
    
