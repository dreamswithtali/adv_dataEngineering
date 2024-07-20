# Amazon S3 Setup

## Steps
1. **Create an S3 Bucket**:
    - Go to S3 in the AWS Management Console.
    - Create a new bucket named `sensor-data-bucket`.
2. **Configure Bucket Policies**:
    - Set up policies to allow access from AWS IoT Core and other services.
3. **Organize Data Storage**:
    - Create folders for raw and processed data.

## Example Policy
```json
{
  "Version": "2024-07-15",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::sensor-data-bucket/*"
    }
  ]
}
