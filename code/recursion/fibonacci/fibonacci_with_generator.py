"""
    smarter fibonacci with a generator
"""


def fibonacci_with_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main():
    for index, fibonacci_number in zip(range(101), fibonacci_with_generator()):
        print(f"{index}: {fibonacci_number}")

if __name__ == "__main__":
    main()
