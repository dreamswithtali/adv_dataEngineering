# Requirements for Assignment 1: Architecture Design and Setup

## Project Overview
Design and set up a real-time sensor data processing platform using AWS services to handle data engineering and processing for various data sizes, including 10MB, 1GB, 10GB, and 100GB.

## High-Level Architecture Components
1. **Data Ingestion**
   - **Service**: AWS IoT Core
   - **Details**: Ingest data from sensors in real-time using MQTT topics.

2. **Data Storage**
   - **Services**: Amazon S3, Amazon Redshift
   - **Details**: Store raw data in S3 and processed data in Redshift.

3. **Data Processing**
   - **Services**: AWS Lambda, AWS Glue
   - **Details**: Real-time processing with Lambda, batch processing with Glue.

4. **Data Aggregation**
   - **Service**: AWS Glue
   - **Details**: Aggregate processed data using Glue jobs.

5. **Data Visualization**
   - **Service**: Amazon QuickSight
   - **Details**: Create dashboards and visualizations for aggregated data.

## GitHub Repository
- **Repository Name**: `Real-Time-Sensor-Data-Platform`
- **Structure**:

Real-Time-Sensor-Data-Platform/
├── README.md
├── architecture-diagram.png
├── data_ingestion/
│ ├── iot-core-setup.md
│ └── iot-core-configuration.json
├── data_storage/
│ ├── s3-setup.md
│ └── redshift-setup.md
├── data_processing/
│ ├── lambda-functions/
│ │ ├── process_data.py
│ │ └── requirements.txt
│ └── glue-jobs/
│ ├── batch_process.py
│ └── glue-configuration.json
├── data_aggregation/
│ └── glue-aggregation-job.py
└── data_visualization/
└── quicksight-setup.md


## AWS Services Setup

### Data Ingestion
- **Setup Instructions**: `data_ingestion/iot-core-setup.md`
- **Configuration File**: `data_ingestion/iot-core-configuration.json`

### Data Storage
- **S3 Setup Instructions**: `data_storage/s3-setup.md`
- **Redshift Setup Instructions**: `data_storage/redshift-setup.md`

### Data Processing
- **Lambda Function**: `data_processing/lambda-functions/process_data.py`
- **Dependencies**: `data_processing/lambda-functions/requirements.txt`
- **Glue Batch Processing**: `data_processing/glue-jobs/batch_process.py`
- **Glue Configuration**: `data_processing/glue-jobs/glue-configuration.json`

### Data Aggregation
- **Glue Aggregation Job**: `data_aggregation/glue-aggregation-job.py`

### Data Visualization
- **QuickSight Setup**: `data_visualization/quicksight-setup.md`

## Architecture Diagram
- **Image**: `architecture-diagram.png`

