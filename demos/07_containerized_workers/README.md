# Containerized Workers Demo

## Build the Task Shared Library

1. Create a new environment and install packages with `pip`.

    ```bash
    cd 07_containerized_workers/apps/task_shared

    micromamba create -n task-shared python=3.11.3

    python -m pip install --upgrade pip

    python -m pip install -r ./requirements.txt
    ```

1. Build and copy the wheel to the other two projects.

    ```bash
    make
    ```

## Build the Task Worker Library

1. Build the Task Worker Docker Image.

    ```bash
    cd 07_containerized_workers/apps/task_worker

    docker build -t task_worker .
    ```

## Run the Servers

1. Bring up the servers with Docker Compose.

    ```bash
    cd 07_containerized_workers

    docker compose up -d
    ```

## Load up the Rabbit MQ Dashboard

1. Open a web browser, and navigate to [http://localhost:8091](http://localhost:8091). Login with the following credentials.

    - Username: brokeruser
    - Password: brokerpass

## Load up the Postgresql Dashboard

1. Open a web browser, and navigate to [http://localhost:8090](http://localhost:8090). Login with the following credentials.

    - Username: dbuser@dbhost.data
    - Password: dbpass

2. Create a new database connection with the following information:

    - Connection Name: database
    - Database Host: database
    - User: postgres
    - Password: <blank>

3. Create a new database named `celery`,

# Run the Task Manager

1. Create a new environment and install the packages with `pip`.

    ```bash
    cd 07_containerized_workers/apps/task_manager

    micromamba create -n task-manager python=3.11.3

    python -m pip install --upgrade pip

    python -m pip install -r ./requirements.txt
    ```

2. Run the Task Manager.

    ```bash
    python -m task_manager
    ```
