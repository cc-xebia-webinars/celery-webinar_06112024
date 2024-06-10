import os

from task_shared.celery_app import create_celery_app
from task_shared.tasks import wire_up_tasks

worker_app = create_celery_app(
    os.environ.get("BROKER_CONN_STR"),
    os.environ.get("RESULT_BACKEND_CONN_STR"),
)
wire_up_tasks(worker_app)
