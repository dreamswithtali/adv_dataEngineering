# Real-Time Sensor Data Platform

## Overview

This project involves designing, setting up, and implementing a real-time sensor data processing platform using AWS services. The platform handles data ingestion, storage, processing, aggregation, and visualization, catering to data sizes from 10MB to 100GB.


### Assignment 2: Data Ingestion and Processing

1. **Implement Data Ingestion**
    - Use AWS Kinesis Data Streams to stream data from a source to Amazon S3.
    - **Script**: `data_ingestion/kinesis_producer.py`

2. **Develop Data Processing Pipeline**
    - Use AWS Glue to process data.
    - **Script**: `data_processing/glue_jobs/data_processing.py`

3. **Apply Data Transformation and Cleansing**
    - Transform and cleanse the data for aggregation and analysis.

4. **Implement Data Partitioning and Indexing**
    - Optimize query performance using data partitioning and indexing strategies.

5. **Update GitHub Repository**
    - Code and configuration files for data ingestion and processing.
