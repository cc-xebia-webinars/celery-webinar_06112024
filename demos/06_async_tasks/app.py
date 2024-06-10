from proj import tasks
import asyncio

# Here's how AsyncResult relates to asyncio in this code:

# 1. Celery's `AsyncResult`: When you call,
#    ```python
#    tasks.add.apply_async((2, 2), countdown=30)
#    ```
#    , it returns an instance of AsyncResult. This object allows you to
#    check the status of the task, retrieve the result, or wait for the
#    task to complete.
# 2. Integration with `asyncio`: The code uses asyncio to handle asynchronous
#    operations. Specifically, it uses asyncio.get_event_loop() to get the
#    current event loop and `loop.run_in_executor(None, async_task.get)` to run
#    the get method of each AsyncResult in a separate thread. This allows the
#    program to wait for the results of the Celery tasks without blocking the main
#    thread.

# In summary, AsyncResult objects are used to track the status and results of Celery tasks, and asyncio is used to manage these objects asynchronously, allowing the program to handle multiple tasks concurrently.

async def main() -> None:
    
    # get_event_loop() returns an instance of the current event loop
    # with an instance of the current event loop, we can call run_in_executor() to
    # run a function in a separate thread and return the result
    loop = asyncio.get_event_loop()

    # apply_async() returns an instance of AsyncResult that lets you inspect the
    # async_tasks = [tasks.add.apply_async((2, 2), countdown=5) for _ in range(100)]
    async_tasks = [tasks.add.apply_async((2, 2),) for _ in range(10000)]

    # run_in_executor() runs a function in a separate thread and returns the result
    # the `async_task.get` function returns the result of the task, once they all
    # complete, the `asyncio.gather` function returns the results in order
    results = await asyncio.gather(
        *[loop.run_in_executor(None, async_task.get) for async_task in async_tasks])

    print(results)

if __name__ == '__main__':
    asyncio.run(main())
