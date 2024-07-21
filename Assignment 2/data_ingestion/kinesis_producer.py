import boto3
import json
import time

kinesis = boto3.client('kinesis', region_name='us-west-2')

def generate_data():
    while True:
        data = {
            'sensor_id': 'sensor_1',
            'timestamp': int(time.time()),
            'value': 100
        }
        
        kinesis.put_record(
            StreamName='my-kinesis-stream',
            Data=json.dumps(data),
            PartitionKey='sensor_1'
        )
        
        time.sleep(1)

if __name__ == '__main__':
    generate_data()
