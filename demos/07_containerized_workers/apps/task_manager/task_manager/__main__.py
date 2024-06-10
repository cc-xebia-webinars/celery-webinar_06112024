import os
from dotenv import load_dotenv

from task_shared.celery_app import create_celery_app
from task_shared.tasks import wire_up_tasks

load_dotenv()

app = create_celery_app(
    os.environ.get("BROKER_CONN_STR"),
    os.environ.get("RESULT_BACKEND_CONN_STR"),
)
fibonacci = wire_up_tasks(app)

for i in range(10000):
    fibonacci.delay(i)
