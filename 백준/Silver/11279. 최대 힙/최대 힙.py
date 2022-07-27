import heapq
import sys
from collections import deque
from queue import PriorityQueue
import heapq


def solution():
    n = int(sys.stdin.readline())

    heap = []

    for _ in range(n):
        num = int(sys.stdin.readline())

        if num != 0:
            heapq.heappush(heap, -num)

        elif num == 0:
            if not heap:
                print(0)
            else:
                print(heapq.heappop(heap) * -1)

    


if __name__ == "__main__":
    solution()
