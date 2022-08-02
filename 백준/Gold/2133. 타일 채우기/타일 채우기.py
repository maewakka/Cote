import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().strip())

n_tile = [0 for i in range(n+1)]

def tile(x):
    if x == 0:
        return 1
    if x == 1:
        return 0
    if x == 2:
        return 3

    if n_tile[x] == 0:
        n_tile[x] = 3 * tile(x-2)
        for i in range(3, x+1):
            if i % 2 == 0:
                n_tile[x] += 2 * tile(x-i)

    return n_tile[x]

print(tile(n))