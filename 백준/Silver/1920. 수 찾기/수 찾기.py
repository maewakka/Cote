import sys

def solution():
    n = int(sys.stdin.readline())
    inputs = list(map(int, sys.stdin.readline().split()))
    nums = {}

    for i in inputs:
        nums[i] = True

    m = int(sys.stdin.readline())
    inputs = list(map(int, sys.stdin.readline().split()))

    for i in inputs:
        if nums.get(i) != None:
            print(1)
        else:
            print(0)


if __name__ == "__main__":
    solution()