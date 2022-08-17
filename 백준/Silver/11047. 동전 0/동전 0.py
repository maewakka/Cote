import sys

def solution():
    N, K = map(int, sys.stdin.readline().strip().split(" "))
    coins = []
    count = 0

    for i in range(N):
        coins.append(int(sys.stdin.readline().strip()))
    while True:
        max_coin = 1
        for i in range(N-1, 0, -1):
            if coins[i] <= K:
                max_coin = coins[i]
                break

        count += K // max_coin
        K = K % max_coin

        if K <= 0:
            break

    print(count)

if __name__ == "__main__":
    solution()