import json

def lambda_handler(event, context):
    """AWS Lambda calculator API"""
    
    try:
        # Get operation and numbers from query params
        operation = event['queryStringParameters']['operation']
        num1 = float(event['queryStringParameters']['num1'])
        num2 = float(event['queryStringParameters']['num2'])
        
        # Calculate
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        else:
            result = "Error: Invalid operation"
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'operation': operation,
                'num1': num1,
                'num2': num2,
                'result': result
            })
        }
    
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }