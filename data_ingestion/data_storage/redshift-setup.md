# Amazon Redshift Setup

## Steps
1. **Create a Redshift Cluster**:
    - Go to Redshift in the AWS Management Console.
    - Create a new cluster and configure it.
2. **Set Up IAM Roles**:
    - Create an IAM role that allows Redshift to access S3.
3. **Configure Data Warehouse**:
    - Set up the schema and tables for storing processed data.

## Example Schema
```sql
CREATE TABLE sensor_data (
    id INT IDENTITY(1,1),
    sensor_id VARCHAR(50),
    timestamp TIMESTAMP,
    data JSON,
    PRIMARY KEY(id)
);
