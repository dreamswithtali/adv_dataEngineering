import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load processed data from S3
datasource0 = glueContext.create_dynamic_frame.from_options(
    connection_type = "s3",
    connection_options = {"paths": ["s3://sensor-data-bucket/processed/"]},
    format = "json"
)

# Aggregation logic
aggregated_df = datasource0.toDF()
aggregated_df = aggregated_df.groupBy("sensor_id").agg({"value": "avg"})

# Convert back to dynamic frame
aggregated_dynamic_frame = DynamicFrame.fromDF(aggregated_df, glueContext, "aggregated_dynamic_frame")

# Write aggregated data to Redshift
glueContext.write_dynamic_frame.from_jdbc_conf(
    frame = aggregated_dynamic_frame,
    catalog_connection = "redshift-connection",
    connection_options = {
        "dbtable": "aggregated_sensor_data",
        "database": "sensor_data_db"
    },
    redshift_tmp_dir = "s3://temp/"
)

job.commit()
