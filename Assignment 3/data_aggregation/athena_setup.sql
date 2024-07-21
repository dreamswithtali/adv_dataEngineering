-- Create a table in Athena
CREATE EXTERNAL TABLE sensor_data (
    id INT,
    sensor_id STRING,
    timestamp TIMESTAMP,
    value DOUBLE
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://your-processed-data-bucket/';

-- Example aggregation query
CREATE TABLE daily_sensor_aggregates AS
SELECT 
    sensor_id,
    date_trunc('day', timestamp) as day,
    avg(value) as average_value
FROM 
    sensor_data
GROUP BY 
    sensor_id, day
ORDER BY 
    day;
