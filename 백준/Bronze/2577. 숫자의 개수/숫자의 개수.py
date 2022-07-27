import sys
from collections import deque

def solution():
    A = int(sys.stdin.readline().strip())
    B = int(sys.stdin.readline().strip())
    C = int(sys.stdin.readline().strip())

    digit = "0123456789"
    result = [0 for i in range(len(digit))]

    number = str(A * B * C)

    for char in number:
        result[int(char)] += 1

    for i in result:
        print(i)



if __name__ == "__main__":
    solution()