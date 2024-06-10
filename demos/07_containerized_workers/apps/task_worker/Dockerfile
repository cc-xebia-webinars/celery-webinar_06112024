FROM python:3.11.3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY task_shared-0.1.0-py3-none-any.whl ./
RUN pip install task_shared-0.1.0-py3-none-any.whl

COPY task_worker/worker.py  .

CMD [ "celery", "-A", "worker", "worker", "--loglevel=INFO" ]