import matplotlib.pyplot as plt
import math


start = 1
end = int(10e8)
step = int(end / 20)
integers = range(start, end, step)


def dec2bin(n):
    # m = int(log(n) / log(2))
    counter = 1
    m = int(math.log2(n))
    # print(m == n)
    liste = [0 for i in range(m + 1)]
    for i in range(m + 1):
        counter += 1
        liste[i] = (n % (2 ** (i + 1))) // (2**i)
    return liste, n, counter


counters = []
for n in integers:
    counters.append(dec2bin(n)[2])


title = "Complexity of decimal to binary conversion"
file = "decimal_to_binary.pdf"
plt.plot(integers, counters, "o")
plt.ylabel("Number of operations")
plt.xlabel("integer to convert")
plt.title(title)
plt.savefig("images/" + file)
plt.close()
