import sys

def solution():
    answer = []

    n = int(sys.stdin.readline())
    nums = {}

    inputs = list(map(int, sys.stdin.readline().split()))
    for input in inputs:
        nums[input] = True

    m = int(sys.stdin.readline())
    inputs = list(map(int, sys.stdin.readline().split()))

    for input in inputs:
        if nums.get(input) == None:
            answer.append('0')
        else:
            answer.append('1')

    print(' '.join(answer))

if __name__ == "__main__":
    solution()