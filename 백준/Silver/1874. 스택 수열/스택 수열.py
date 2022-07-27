import sys
from collections import deque


def solution():
    n = int(sys.stdin.readline())

    stack = []
    result = []
    index = 1

    for _ in range(n):
        this_num = int(sys.stdin.readline())

        if this_num >= index:
            for _ in range(this_num-index+1):
                stack.append(index)
                index += 1
                result += '+'

        if this_num < index:
            while stack and this_num == stack[-1]:
                stack.pop()
                result += '-'

    if not stack:
        for cal in result:
            print(cal)
    else:
        print("NO")



if __name__ == "__main__":
    solution()
