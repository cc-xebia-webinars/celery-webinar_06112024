from proj import tasks
import time


def main() -> None:
    add_results = tasks.add.apply_async((2, 2), countdown=20)
    mul_results = tasks.mul.apply_async((2, 4), countdown=20)
    xsum_results = tasks.xsum.apply_async(([1,2,3,4,5],), countdown=20)

    while not all([add_results.ready(), mul_results.ready(), xsum_results.ready()]):
        time.sleep(2)
        print("waiting for results...")

    print(add_results.get(timeout=1))
    print(mul_results.get(timeout=1))
    print(xsum_results.get(timeout=1))
    

if __name__ == '__main__':
    main()

