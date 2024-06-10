from celery import Celery

app = Celery('proj',
             broker='pyamqp://brokeruser:brokerpass@localhost:5091//',
             backend='db+postgresql://postgres:postgres@localhost:5090/celery',
             include=['proj.tasks'])

app.conf.update(result_expires=3600)

if __name__ == '__main__':
    app.start()