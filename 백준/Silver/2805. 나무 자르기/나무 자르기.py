import sys

def solution():
    n, m = map(int, sys.stdin.readline().split())
    trees = list(map(int, sys.stdin.readline().split()))

    left, right = 1,max(trees)

    while left <= right:
        mid = (left + right) // 2
        total = 0
        for t in trees:
            if t > mid:
                total += (t - mid)

        if total < m:
            right = mid - 1
        else:
            left = mid + 1

    print(right)



if __name__ == "__main__":
    solution()