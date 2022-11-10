"""
    same function as recursive function but
    written in a dynamic programming way
"""

m = 30
n = 30

liste = [[0 for i in range(m + 1)] for j in range(n + 1)]
liste[0] = [i for i in range(m + 1)]
for j in range(1, n + 1):
    liste[j][0] = j
    for i in range(1, m + 1):
        liste[j][i] = liste[j - 1][i] + liste[j][i - 1]
print(liste[30][30])
