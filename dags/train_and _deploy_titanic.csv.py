import airflow.utils.dates
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflor_and_aws.extract import extract_titanic_data
from airflow.providers.amazon.aws.operators.s3_copy_object import S3CopyObjectOperator
from airflow.providers.amazon.aws.operators.sagemaker_endpoint import SageMakerEndpointOperator
from airflow.providers.amazon.aws.operators.sagemaker_training import SageMakerTraininOperator
from airflow.decorators import dag, task
from airflow.utils.edgemodifier import Label

from datetime import datetime, timedelta

default_args ={
    'owner': 'Camilo',
    'start_date': airflow.utils.dates.days_ago(3),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=3),
    }
@dag(
    ag_id='deploy a model with airflow and aws',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='DAG to train and deploy a titanic classifier'

)

def s3_copy_operator_decorator(task_id:str, source_bucket_name: str, source_bucket_key:str, dest_bucket_name:str, dest_bucket_key:str) -> None:
    @task(task_id=task_id)
    def s3_copy_operator_task():
        return S3CopyObjectOperator(
            task_id=task_id,
            source_bucket_name=source_bucket_name,
            source_bucket_key=source_bucket_key,
            dest_bucket_name=dest_bucket_name,
            dest_bucket_key=dest_bucket_key,
            dag=dag
        )
    return s3_copy_operator_task

def sagemaker_training_operator_decorator(task_id:str, config:dict) -> None:
    @task(task_id=task_id)
    def sagemaker_training_operator_task():
        return SageMakerTrainingOperator(
            task_id=task_id,
            config=config,
            wait_for_completion=True,
            print_log=True,
            check_interval=10,
            dag=dag
        )
    return sagemaker_training_operator_task

def sagemaker_endpoint_operator_decorator(task_id, config):
    @task(task_id=task_id)
    def sagemaker_endpoint_operator_task():
        return SageMakerEndpointOperator(
            task_id=task_id,
            wait_for_completion=True,
            config=config,
            dag=dag
        )
    return sagemaker_endpoint_operator_task

# Example usage of decorators
download_date_task = s3_copy_operator_decorator(
    task_id='download_data_titanic',
    source_bucket_name='',
    source_bucket_key='',
    dest_bucket_name='DeployBucket',
    dest_bucket_key='titanic.pkl.gz'
)()

sagemaker_train_model_task = sagemaker_training_operator_decorator(
    task_id='train_model',
    config={
        "TrainingJobName": "titaclassifier-{{ execution_date.strftime('%Y-%m-%d-%H-%M-%S') }}",
        "AlgorithmSpecification": {
            "TrainingImage": "683313688378.dkr.ecr.us-west-2.amazonaws.com/randomforest:latest",  # Imagen para RandomForest
            "TrainingInputMode": "File",
        },
        "HyperParameters": {
            "max_depth": "63",
            "max_samples": "100"
        },
        "InputDataConfig": [
            {
                "ChannelName": "train",
                "DataSource": {
                    "S3DataSource": {
                        "S3DataType": "S3Prefix",
                        "S3Uri": "s3://DeployBucket/tita_data",
                        "S3DataDistributionType": "FullyReplicated",
                    },
                },
            },
        ],
        "OutputDataConfig": {"S3OutputPath": "s3://DeployBucket/titaclassifier-output"},
        "ResourceConfig": {
            "InstanceType": "ml.c4.xlarge",
            "InstanceCount": 1,
            "VolumeSizeInGB": 10,
        },
        "RoleArn": "arn:aws:iam::297623009465:role/service-role/AmazonSageMaker-ExecutionRole-20180905T153196",
        "StoppingCondition": {"MaxRuntimeInSeconds": 15 * 30 * 30},
    }
    
)()

sagemaker_deploying_model_task = sagemaker_endpoint_operator_decorator(
    task_id="deploy_model",
    config={
            "Model": {
                "ModelName": "titaclassifier-{{ execution_date.strftime('%Y-%m-%d-%H-%M-%S') }}",
                "PrimaryContainer": {
                    "Image": "438346466558.dkr.ecr.eu-west-1.amazonaws.com/randomforest:latest",
                    "ModelDataUrl": (
                        "s3://DeployBucket/titaclassifier-output/"
                        "mnistclassifier-{{ execution_date.strftime('%Y-%m-%d-%H-%M-%S') }}/output/model.tar.gz"
                    ),
                },
                "ExecutionRoleArn": "arn:aws:iam::297623009465:role/service-role/AmazonSageMaker-ExecutionRole-20180905T153196",
            },
            "EndpointConfig": {
                "EndpointConfigName": "mnistclassifier-{{ execution_date.strftime('%Y-%m-%d-%H-%M-%S') }}",
                "ProductionVariants": [
                    {
                        "InitialInstanceCount": 1,
                        "InstanceType": "ml.t2.medium",
                        "ModelName": "titaclassifier",
                        "VariantName": "AllTraffic",

                    }
                ],
            },
            "Endpoint": {
                "EndpointConfigName": "mnistclassifier-{{ execution_date.strftime('%Y-%m-%d-%H-%M-%S') }}",
                "EndpointName": "mnistclassifier",
            },
        }
)()

processing_data = PythonOperator(
    task_id='processing_data',
    python_callable=extract_titanic_data,
    dag=dag
)

# Task dependencies
Label("download_date_task") >> Label('processing_data') >> Label('sagemaker_train_model_task') >> Label('sagemaker_deploying_model_task')

