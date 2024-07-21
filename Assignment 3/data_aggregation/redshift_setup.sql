-- Create a table in Redshift
CREATE TABLE sensor_data (
    id INT IDENTITY(1,1),
    sensor_id VARCHAR(50),
    timestamp TIMESTAMP,
    value DOUBLE PRECISION,
    PRIMARY KEY(id)
);

-- Example aggregation query
CREATE VIEW daily_sensor_aggregates AS
SELECT 
    sensor_id,
    DATE_TRUNC('day', timestamp) as day,
    AVG(value) as average_value
FROM 
    sensor_data
GROUP BY 
    sensor_id, day
ORDER BY 
    day;
