from celery import Celery
from kombu import Exchange, Queue

app = Celery('proj',
             broker='pyamqp://brokeruser:brokerpass@localhost:5091//',
             backend='db+postgresql://postgres:postgres@localhost:5090/celery',
             include=['proj.tasks'])

app.conf.task_queues = (
    Queue('cobalt', Exchange('cobalt'), routing_key='cobalt'),
    Queue('cosmic', Exchange('cosmic'), routing_key='cosmic'),
)

app.conf.update(
    result_expires=3600,
    task_routes={
        'proj.tasks.add': {'queue': 'cobalt'},
        'proj.tasks.mul': {'queue': 'cobalt'},
        'proj.tasks.xsum': {'queue': 'cosmic'},
    }    
)

if __name__ == '__main__':
    app.start()