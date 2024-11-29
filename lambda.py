import json

def lambda_handler(event, context):

    # print event
    print(f"event: {json.dumps(event)}")

    # Read query parameters
    query_parameters = event.get('queryStringParameters', {})  # Safely get 'queryStringParameters'

    # Extract 'param1' value
    param1 = query_parameters.get('param1')  # Use .get() to access keys safely

    # Print 'param1'
    print(f"param1: {param1}")

    #add param1 

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from HTW!'+param1)
    }
