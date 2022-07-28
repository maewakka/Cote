import heapq
import sys
from collections import deque
from queue import PriorityQueue
import heapq


def solution():
    N, K = map(int, sys.stdin.readline().strip().split(" "))
    array = list(map(int, sys.stdin.readline().strip().split(" ")))

    array.sort()

    print(array[K-1])


if __name__ == "__main__":
    solution()
