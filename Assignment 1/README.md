# Real-Time Sensor Data Platform

https://github.com/dreamswithtali/adv_dataEngineering/tree/main/Assignment%201

## Assignment 1: Architecture Design and Setup

### Project Overview

Design and set up a real-time sensor data processing platform using AWS services to handle data engineering and processing for various data sizes, including 10MB, 1GB, 10GB, and 100GB.

### Architecture Diagram

![Architecture Diagram](architecture-diagram.png)

### High-Level Architecture

#### 1. Data Ingestion
**Service Used**: AWS IoT Core  
AWS IoT Core is used to ingest data from various sensors in real-time. The data is sent to MQTT topics configured within IoT Core.

#### 2. Data Storage
**Services Used**: Amazon S3 and Amazon Redshift  
Raw data is stored in Amazon S3. Processed data is stored in Amazon Redshift for efficient querying and analysis.

#### 3. Data Processing
**Services Used**: AWS Lambda and AWS Glue  
Real-time data processing is handled by AWS Lambda functions. Batch processing and data transformation are performed using AWS Glue.

#### 4. Data Aggregation
**Service Used**: AWS Glue  
AWS Glue jobs are used to aggregate processed data and prepare it for visualization and analysis.

#### 5. Data Visualization
**Service Used**: Amazon QuickSight  
Amazon QuickSight is used to create interactive dashboards and visualizations for the aggregated sensor data.

### GitHub Repository

- **Repository Name**: `Real-Time-Sensor-Data-Platform`
- **Structure**:

### AWS Services Setup

#### Data Ingestion
- **Setup Instructions**: Detailed in `data_ingestion/iot-core-setup.md`
- **Configuration File**: `data_ingestion/iot-core-configuration.json`

#### Data Storage
- **S3 Setup Instructions**: Detailed in `data_storage/s3-setup.md`
- **Redshift Setup Instructions**: Detailed in `data_storage/redshift-setup.md`

#### Data Processing
- **Lambda Function**: `data_processing/lambda-functions/process_data.py`
- **Dependencies**: `data_processing/lambda-functions/requirements.txt`
- **Glue Batch Processing**: `data_processing/glue-jobs/batch_process.py`
- **Glue Configuration**: `data_processing/glue-jobs/glue-configuration.json`

#### Data Aggregation
- **Glue Aggregation Job**: `data_aggregation/glue-aggregation-job.py`

#### Data Visualization
- **QuickSight Setup**: Detailed in `data_visualization/quicksight-setup.md`

### Architecture Diagram
- **Image**: `architecture-diagram.png`
