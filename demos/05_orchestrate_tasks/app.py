from celery import group, chain, chord
from proj import tasks


def main() -> None:
    # result = tasks.add.delay(4, 4)
    # while not result.ready():
    #     print("waiting...")
    # print(result.get(timeout=1))

    # group - calls a list of tasks in parallel, and it returns a special result
    #         instance that lets you inspect the results as a group, and retrieve
    #         the return values in order
    results = group(tasks.add.s(i, i) for i in range(10))().get()
    print(results)

    # chain - calls a list of tasks in sequence, and it returns a special result
    results = chain(tasks.add.s(4, 4) | tasks.mul.s(8))().get()
    print(results)

    # chord - calls a list of tasks in parallel, with a final callback
    results = chord((tasks.add.s(i, i) for i in range(10)), tasks.xsum.s())().get()
    print(results)

if __name__ == '__main__':
    main()
