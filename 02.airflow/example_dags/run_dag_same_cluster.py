import os
from datetime import timedelta,datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


#pip install spark-on-k8s on airflow first

def my_function(name):
    from spark_on_k8s.client import ExecutorInstances, PodResources, SparkOnK8S, KubernetesClientManager
    # client = SparkOnK8S()
    client = SparkOnK8S(k8s_client_manager = KubernetesClientManager(in_cluster=1))
    client.submit_app(
        image="bill/spark:0.0.1",
        app_path=f"s3a://bill/{name}.py",
        app_arguments=["arg1", "arg2"],
        app_name=f"spark-job_{name}",
        namespace="spark-operator",
        service_account="spark-driver",
        app_waiter="log",
        image_pull_policy="IfNotPresent",
        ui_reverse_proxy=True,
        driver_resources=PodResources(cpu=1, memory=1048, memory_overhead=128),
        executor_resources=PodResources(cpu=1, memory=2048, memory_overhead=128),
        executor_instances=ExecutorInstances(initial=1),
    )

with DAG(
    "testing",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple tutorial DAG",
    schedule=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    t1 = PythonOperator(
    task_id='spark_submit1',
    python_callable= my_function,
    op_kwargs={'name': 'test2'},
    dag=dag,
    )

    t2 = PythonOperator(
    task_id='spark_submit2',
    python_callable= my_function,
    op_kwargs={'name': 'test4'},
    dag=dag,
    )

    t3 = PythonOperator(
    task_id='spark_submit3',
    python_callable= my_function,
    op_kwargs={'name': 'test5'},
    dag=dag,
    )
    t1 >> t2
    t3