import heapq
import sys
from collections import deque
from queue import PriorityQueue
import heapq


def solution():
    n = int(sys.stdin.readline())
    array = []

    origin_index = [i for i in range(1, n+1)]


    for i in range(n):
        array.append([int(sys.stdin.readline()), i])

    array.sort()

    answer = []

    for i in range(n):
        answer.append(array[i][1] - i)

    print(max(answer)+1)

if __name__ == "__main__":
    solution()
