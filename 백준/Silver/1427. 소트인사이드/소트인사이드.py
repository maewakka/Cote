import heapq
import sys
from collections import deque
from queue import PriorityQueue
import heapq


def solution():
    n = sys.stdin.readline().strip()

    int_list = []
    answer = []

    for i in range(len(n)):
        int_list.append(int(n[i]))

    for i in range(len(n)):
        temp = max(int_list[i:])
        int_list[int_list[i:].index(temp)+i] = int_list[i]
        int_list[i] = temp
        answer.append(temp)

    print(''.join(list(map(str, answer))))


if __name__ == "__main__":
    solution()
