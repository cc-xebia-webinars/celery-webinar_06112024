from celery import Celery


def create_celery_app(broker_conn_str, result_backend_conn_str):
    return Celery(
        "task_tool",
        broker=broker_conn_str,
        result_backend=result_backend_conn_str,
    )
