 # Deploy a Model with Airflow and AWS

This repository contains code for a DAG (Directed Acyclic Graph) that uses Airflow to orchestrate the training and deployment of a Random Forest model for the Titanic dataset using Amazon SageMaker. The DAG is defined in `deploy_a_model_with_airflow_and_aws.py`.

## Step-by-Step Explanation of the Code

### 1. Importing Necessary Libraries

```python
import airflow.utils.dates
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflor_and_aws.extract import extract_titanic_data
from airflow.providers.amazon.aws.operators.s3_copy_object import S3CopyObjectOperator
from airflow.providers.amazon.aws.operators.sagemaker_endpoint import SageMakerEndpointOperator
from airflow.providers.amazon.aws.operators.sagemaker_training import SageMakerTraininOperator

from datetime import datetime, timedelta
```

This code imports the necessary libraries and modules for creating the DAG and performing the data extraction, training, and deployment tasks.

### 2. Defining Default Arguments

```python
default_args ={
    'owner': 'Camilo',
    'start_date': airflow.utils.dates.days_ago(3),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=3),
    }
```

These are the default arguments for the DAG. They specify the owner of the DAG, the start date, whether it depends on past DAG runs, the number of retries, and the retry delay.

### 3. Defining the DAG

```python
with DAG (
    dag_id='deploy a model with airflow and aws',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='DAG to train and deploy a titanic classifier',
    ) as dag:
```

This code defines the DAG with the specified dag_id, default arguments, schedule interval, catchup flag, and description.

### 4. Downloading Data from Amazon S3 Bucket

```python
download_date=S3CopyObjectOperator(
    task_id='download_data_titanic',
    source_bucket_name='',
    source_bucket_key='',
    
