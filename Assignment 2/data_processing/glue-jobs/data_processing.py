import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource0 = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://example-input-bucket/sensor-data/"]},
    format="json"
)

applymapping1 = ApplyMapping.apply(
    frame=datasource0,
    mappings=[
        ("sensor_id", "string", "sensor_id", "string"),
        ("timestamp", "long", "timestamp", "timestamp"),
        ("value", "double", "value", "double")
    ]
)

datasink2 = glueContext.write_dynamic_frame.from_options(
    frame=applymapping1,
    connection_type="s3",
    connection_options={"path": "s3://example-output-bucket/sensor-data/processed/"},
    format="json"
)

job.commit()
