# Multiple Queues Demo

## Start the Broker and Backend

1. Change into the `04_multiple_queues` folder.

    ```bash
    cd 04_multiple_queues
    ```

1. Start the servers with Docker Compose in daemon mode.

    ```bash
    docker compose up -d
    ```

1. View the RabbitMQ service and queues with the web-based admin tool.

    - URL: [http://localhost:8091](http://localhost:8091)
    - Username: brokeruser
    - Password: brokerpass

1. Register the database server and create a new database named `celery`.

    - URL: [http://localhost:8090](http://localhost:8090)
    - Username: dbuser@dbhost.data
    - Password: dbpass
    - New Server Hostname: database
    - New Server Username: postgres
    - New Database Name: celery

1. Review the files in the `proj` folder.

## Stop the Broker

1. Bring down the broker and backend containers and delete the volumes.

    ```bash
    docker compose down -v
    ```
