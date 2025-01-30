from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def fibonachi(n):
    if n <= 1:
        return 1
    return fibonachi(n - 1) + fibonachi(n - 2)


def task() -> int:
    return fibonachi(40)


def the_end() -> str:
    return "The end!"


default_args = {'retries': 3}

with DAG(
    dag_id="dag-with-many-tasks",
    default_args=default_args,
    schedule_interval=None,
    start_date=datetime.today(),
    tags=['huge-dag'],
) as dag:
    for i in range(1, 31):
        PythonOperator(task_id=f"task-{i}", python_callable=task)

    list(dag.tasks) >> PythonOperator(
        task_id="the_end",
        python_callable=the_end,
    )


