

import json
import boto3

def lambda_handler(event, context):
    # Process the incoming data
    data = json.loads(event['body'])
    
    # Transform the data as required
    processed_data = transform_data(data)
    
    # Store the processed data in S3
    s3 = boto3.client('s3')
    s3.put_object(Bucket='sensor-data-bucket', Key='processed/data.json', Body=json.dumps(processed_data))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data processed successfully')
    }

def transform_data(data):
    # Example transformation logic
    transformed_data = {
        'sensor_id': data['sensor_id'],
        'timestamp': data['timestamp'],
        'value': data['value'] * 2  # Example transformation
    }
    return transformed_data
