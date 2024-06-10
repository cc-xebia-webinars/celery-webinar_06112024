from celery import Celery
from celery.local import PromiseProxy

def fibonacci(length: int) -> int:
    if length <= 0:
        return 0
    elif length == 1:
        return 1
    
    fib_sequence = [0, 1]
    while len(fib_sequence) < length:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return sum(fib_sequence)


def wire_up_tasks(app: Celery) -> tuple[PromiseProxy]:
    return app.task(fibonacci)
