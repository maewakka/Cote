import sys
from collections import deque

def solution():
    N = int(sys.stdin.readline().strip())

    alpahbet = "abcedfghijklmnopqrstuvwxyz"


    for i in range(N):
        left = [0 for i in range(len(alpahbet))]
        right = [0 for i in range(len(alpahbet))]

        com = sys.stdin.readline().strip().split(' ')

        for j in com[0]:
            left[alpahbet.find(j)] += 1

        for j in com[1]:
            right[alpahbet.find(j)] += 1

        if left == right:
            print('Possible')
        else:
            print('Impossible')


if __name__ == "__main__":
    solution()