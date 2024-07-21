 Real-Time Sensor Data Platform

## Overview

This project involves designing, setting up, and implementing a real-time sensor data processing platform using AWS services. The platform handles data ingestion, storage, processing, aggregation, and visualization, catering to data sizes from 10MB to 100GB.

## Assignments

### Assignment 2: Architecture Design and Setup

1. **Design High-Level Architecture**
    - Components: Data Ingestion (AWS IoT Core), Data Storage (Amazon S3, Amazon Redshift), Data Processing (AWS Lambda, AWS Glue), Data Aggregation (AWS Glue), Data Visualization (Amazon QuickSight)
    - ![Architecture Diagram](architecture-diagram.png)

2. **GitHub Repository Setup**
    - Repository: `Real-Time-Sensor-Data-Platform`

3. **README.md**
    - Overview of the project and architecture diagram.

4. **AWS Services Setup**
    - AWS IoT Core, S3, Lambda, Glue, Redshift, QuickSight.


5. **Implement Data Ingestion**
    - Use AWS Kinesis Data Streams to stream data from a source to Amazon S3.
    - **Script**: `data_ingestion/kinesis_producer.py`

6. **Develop Data Processing Pipeline**
    - Use AWS Glue to process data.
    - **Script**: `data_processing/glue_jobs/data_processing.py`

7. **Apply Data Transformation and Cleansing**
    - Transform and cleanse the data for aggregation and analysis.

8. **Implement Data Partitioning and Indexing**
    - Optimize query performance using data partitioning and indexing strategies.

5. **Update GitHub Repository**
    - Code and configuration files for data ingestion and processing.
