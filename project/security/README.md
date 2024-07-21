# Security Configuration

## S3 Bucket Policy

This policy ensures proper access control for the `sensor-data-bucket` S3 bucket.

### s3_bucket_policy.json

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::sensor-data-bucket",
        "arn:aws:s3:::sensor-data-bucket/*"
      ]
    }
  ]
}
