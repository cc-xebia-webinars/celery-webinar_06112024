#!/bin/sh

celery multi stop w1 -A proj -l INFO -Q cobalt --pidfile=processes/%n.cobalt.pid --logfile=processes/%n%I.cobalt.log
celery multi stop w1 -A proj -l INFO -Q cosmic --pidfile=processes/%n.cosmic.pid --logfile=processes/%n%I.cosmic.log
