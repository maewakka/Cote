import sys

def solution():
    k, n = map(int, sys.stdin.readline().split())

    lans = []
    answer = 0
    for i in range(k):
        lans.append(int(sys.stdin.readline()))

    left, right = 1, max(lans)
    while left <= right:
        mid = (left + right) // 2

        count = 0
        for lan in lans:
            count += lan // mid

        if count >= n:
            left = mid + 1
        else:
            right = mid - 1

    print(right)

if __name__ == "__main__":
    solution()