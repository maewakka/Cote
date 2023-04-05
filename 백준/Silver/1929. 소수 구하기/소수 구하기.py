import sys
import math

def solution():
    n, m = map(int, sys.stdin.readline().split())
    nums = [True for i in range(0, m+1)]
    nums[0] = False
    nums[1] = False

    for i in range(2, round(math.sqrt(m))+1):
        for j in range(i*2, m+1, i):
            nums[j] = False

    for i, result in enumerate(nums):
        if i >= n and result:
            print(i)


if __name__ == "__main__":
    solution()