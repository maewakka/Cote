import sys
from collections import deque


def solution():
    n = int(sys.stdin.readline())

    Array = list(map(int, sys.stdin.readline().split(' ')))
    stack = []
    answer = [-1 for i in range(n)]

    stack.append(0)
    index = 1

    for i in range(1, n):
        while stack and Array[i] > Array[stack[-1]]:
            if stack and Array[i] > Array[stack[-1]]:
                answer[stack.pop()] = Array[i]
        stack.append(i)


    print(*answer)



if __name__ == "__main__":
    solution()
