# AWS IoT Core Setup

## Steps

1. **Create an IoT Core Thing**:
    - Go to AWS IoT Core in the AWS Management Console.
    - Click on "Manage" and then "Things".
    - Click on "Create" and follow the prompts to create a new thing.
    - Name your thing (e.g., `SensorThing`).

2. **Set Up Certificates and Policies**:
    - After creating the thing, click on it and navigate to the "Security" tab.
    - Create a new certificate and download it along with the private key, public key, and root CA.
    - Attach a policy to the certificate to allow data ingestion. A sample policy is provided below:
    
    ```json
    {
      "Version": "2024-07-15",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "iot:Publish",
            "iot:Receive"
          ],
          "Resource": [
            "arn:aws:iot:your-region:your-account-id:topic/sensor/data"
          ]
        }
      ]
    }
    ```

3. **Configure MQTT Topics**:
    - Set up MQTT topics for sensor data ingestion.
    - Go to "Message routing" and click on "Create a rule".
    - Set the SQL statement to `SELECT * FROM 'sensor/data'` to route all incoming messages from the `sensor/data` topic.

4. **Test the Configuration**:
    - Use AWS IoT Core's test feature to verify data ingestion.
    - Navigate to the "Test" section in AWS IoT Core.
    - Subscribe to the topic `sensor/data` and publish a test message to ensure data is being ingested correctly.

## Configuration File
- A sample configuration file `iot-core-configuration.json` is provided below:

```json
{
  "thingName": "SensorThing",
  "certificateArn": "arn:aws:iot:region:account-id:cert/unique-cert-id",
  "policyName": "SensorPolicy",
  "mqttTopic": "sensor/data"
}
