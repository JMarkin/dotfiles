from time import time


def fib():
    a, b = 0, 1
    while True:  # First iteration:
        yield a  # yield 0 to start with and then
        a, b = b, a + b  # a will now be 1, and b will also be 1, (0 + 1)


t = time()
for index, fibonacci_number in zip(range(100), fib()):
    ti = time()
    print("{i:3}: {f: >21} {t:.3e}".format(i=index, f=fibonacci_number, t=ti - t))
    t = ti
