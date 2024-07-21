# Data Retention Configuration

## S3 Lifecycle Policy

This policy ensures proper data retention management for the `sensor-data-bucket` S3 bucket.

### s3_lifecycle_policy.json

```json
{
  "Rules": [
    {
      "ID": "MoveToGlacier",
      "Prefix": "",
      "Status": "Enabled",
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "GLACIER"
        }
      ],
      "Expiration": {
        "Days": 365
      }
    }
  ]
}
