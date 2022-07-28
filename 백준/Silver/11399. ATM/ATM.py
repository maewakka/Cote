import heapq
import sys
from collections import deque
from queue import PriorityQueue
import heapq


def solution():
    n = sys.stdin.readline().strip()

    p_array = list(map(int, sys.stdin.readline().strip().split(' ')))

    p_array.sort()
    answer = 0

    for i in range(int(n)):
        answer += sum(p_array[:i+1])

    print(answer)


if __name__ == "__main__":
    solution()
