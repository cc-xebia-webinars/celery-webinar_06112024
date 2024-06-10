from celery import Celery

# first terminal
# celery -A tasks worker --loglevel=INFO

# second terminal
# start a Python REPL session and run the following Python commands:
# ```python
# >>> from tasks import add
# >>> result = add.delay(4,4)
# >>> result.get(timeout=1)
# ```

app = Celery(
    'tasks',
    broker='pyamqp://brokeruser:brokerpass@localhost:5091//',
    result_backend='db+postgresql://postgres:postgres@localhost:5090/celery')

@app.task
def add(x, y):
    return x + y
