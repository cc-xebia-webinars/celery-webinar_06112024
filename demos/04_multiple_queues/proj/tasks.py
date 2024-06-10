from .celery import app

# ```bash
# python
#
# from proj import tasks
#
# result = tasks.add.delay(4, 4)
# result.ready()
# result.get(timeout=1)
#
# result = tasks.xsum.delay([1, 2, 3, 4])
# result.ready()
# result.get(timeout=1)
#

# ````


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)