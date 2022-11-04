import sys

# sys.setrecursionlimit(int(1e5))
sys.setrecursionlimit(int(1e3))


def badrec(x, depth):
    if x > 0:
        print(x / 2)
        print(depth)
        return badrec(x / 2, depth + 1)
    else:
        return 1


print(badrec(3, 0))
