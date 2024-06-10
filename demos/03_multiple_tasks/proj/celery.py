from celery import Celery

# celery -A proj worker -l INFO

# celery multi start w1 -A proj -l INFO --pidfile=processes/%n.pid --logfile=processes/%n%I.log
# celery multi restart w1 -A proj -l INFO --pidfile=processes/%n.pid --logfile=processes/%n%I.log
# celery multi stop w1 -A proj -l INFO --pidfile=processes/%n.pid --logfile=processes/%n%I.log
# celery multi stopwait w1 -A proj -l INFO --pidfile=processes/%n.pid --logfile=processes/%n%I.log

app = Celery('proj',
             broker='pyamqp://brokeruser:brokerpass@localhost:5091//',
             backend='db+postgresql://postgres:postgres@localhost:5090/celery',
             include=['proj.tasks'])

app.conf.update(result_expires=3600)

if __name__ == '__main__':
    app.start()