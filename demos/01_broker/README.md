# Broker Demo

## Start the Broker

1. Change into the `01_broker` folder.

    ```bash
    cd 01_broker
    ```

1. Start the servers with Docker Compose in daemon mode.

    ```bash
    docker compose up -d
    ```

1. View the RabbitMQ service and queues with the web-based admin tool.

    - URL: [http://localhost:8091](http://localhost:8091)
    - Username: brokeruser
    - Password: brokerpass

1. Review `tasks.py`.

## Stop the Broker

1. Bring down the broker docker containers.

    ```bash
    docker compose down
    ```
