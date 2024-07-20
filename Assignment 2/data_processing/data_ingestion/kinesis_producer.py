import boto3
import json
import time

# Initialize a Kinesis client
kinesis = boto3.client('kinesis', region_name='your-region')

def generate_data():
    while True:
        # Generate sample sensor data
        data = {
            'sensor_id': 'sensor_1',
            'timestamp': int(time.time()),
            'value': 100  # Sample data value
        }
        
        # Put the data into the Kinesis stream
        kinesis.put_record(
            StreamName='your-kinesis-stream-name',
            Data=json.dumps(data),
            PartitionKey='partition_key'
        )
        
        # Wait for a second before sending the next data point
        time.sleep(1)  # Adjust the sleep time as needed

if __name__ == '__main__':
    generate_data()
