"""
    smarter fibonacci with a generator
"""


def smarter_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for index, fibonacci_number in zip(range(101), smarter_fibonacci()):
    print(f"{index}: {fibonacci_number}")
