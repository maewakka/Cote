import sys
import re

def solution():
    N = sys.stdin.readline()
    array = list(map(int, sys.stdin.readline().strip().split(" ")))
    find = int(sys.stdin.readline())

    result = 0

    for num in array:
        if num == find:
            result += 1

    print(result)

if __name__ == "__main__":
    solution()