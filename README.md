# Celery-Powered Python: Empowering Distributed Task Automation

![Xebia Logo](https://imagedelivery.net/VKawrzTPdVOU6XYN26Rvmg/80a8db15-9456-4922-1fb5-ccfaa2e30500/public "Xebia Logo")

We’re not your usual experts. We are rebellious game-changers and professional knowledge-sharers. And quite fun, if we say so ourselves. Invest in your personal learning journey or upskill your entire organization by learning the tech skills of the future. Learn today to get ready for tomorrow!

[Learn More >>>](https://xebia.com/academy)

## Webinar Slides

[Download Slides](./docs/slides.pdf)

## Python Environment Setup

1. Create a new virtual environment.

1. Install the following packages:

    - ruff
    - mypy
    - celery
    - kombu
    - sqlalchemy
    - psycopg2
    - celery-stubs (pip only)

    __>> Terminal commands to create an environment with Micromamba__

    ```bash
    micromamba create -y --name celery-demos python=3.12.3 ruff mypy celery kombu sqlalchemy psycopg2

    micromamba activate celery-demos
    
    python -m pip install celery-stubs
    ```

    __>> Terminal commands to create an environment with Conda__

    ```bash
    conda create -y --name celery-demos python=3.12.3 ruff mypy celery kombu sqlalchemy psycopg2

    conda activate celery-demos
    
    python -m pip install celery-stubs
    ```

    __>> Terminal commands to create an environment with Conda__

    ```bash
    python -m venv venv

    source ./venv/bin/activate

    python -m pip install ruff mypy celery kombu sqlalchemy psycopg2 celery-stubs
    ```    


## Celery Demos

1. [Run a Broker](./demos/01_broker/README.md)
1. [Run a Broker and Backend](./demos/02_broker_and_backend/README.md)
1. [Multiple Tasks](./demos/03_multiple_tasks/README.md)
1. [Multiple Queues](./demos/04_multiple_queues/README.md)
1. [Orchestrate Tasks](./demos/05_orchestrate_tasks/README.md)
1. [Asynchronous Tasks](./demos/06_async_tasks/README.md)
1. [Containerized Workers](./demos/07_containerized_workers/README.md)


## License

The content of this repository is made available under the following [license](LICENSE).

<br>
Course content and teaching is provided by:<br>

[![Cloud Contraptions Logo](https://imagedelivery.net/VKawrzTPdVOU6XYN26Rvmg/aff3f165-00ec-4130-83d3-7ff4744f7d00/h=40,sharpen=1 "Cloud Contraptions Logo")](https://www.cloudcontraptions.com)

<br>
Dev Container image is provided by:<br>

[![Training 4 Programmers Logo](https://imagedelivery.net/VKawrzTPdVOU6XYN26Rvmg/1d56b364-4858-4cc6-84d5-89e14ce8e100/h=40,sharpen=1 "Training 4 Programmers Logo")](https://www.training4programmers.com)
