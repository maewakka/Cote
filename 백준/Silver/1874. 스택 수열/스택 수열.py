import sys
from collections import deque

def solution():
    n = int(sys.stdin.readline())
    inputs = []
    stack = []
    answer = []
    nums = deque([i for i in range(1, n+1)])
    isPos = True

    for _ in range(n):
        inputs.append(int(sys.stdin.readline()))

    index = 0
    while True:
        if not stack and index == n:
            break

        if not stack or stack[-1] != inputs[index]:
            if not nums:
                isPos = False
                break
            else:
                stack.append(nums.popleft())
                answer.append('+')
        else:
            stack.pop()
            index += 1
            answer.append('-')

    if isPos:
        for a in answer:
            print(a)
    else:
        print("NO")


if __name__ == "__main__":
    solution()