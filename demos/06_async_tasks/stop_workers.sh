#!/bin/sh

celery multi stopwait w1 -A proj -l INFO --pidfile=processes/%n.a.pid --logfile=processes/%n%I.a.log
celery multi stopwait w1 -A proj -l INFO --pidfile=processes/%n.b.pid --logfile=processes/%n%I.b.log
celery multi stopwait w1 -A proj -l INFO --pidfile=processes/%n.c.pid --logfile=processes/%n%I.c.log
