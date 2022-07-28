import heapq
import sys
from collections import deque
from queue import PriorityQueue
import heapq
sys.setrecursionlimit(10 ** 7)

def solution():
    N = int(sys.stdin.readline().strip())
    first = [2, 3, 5, 7]

    def DFS(pre_num):
        if len(str(pre_num)) == N:
            print(pre_num)
            return

        for i in range(10):
            isP = True
            number = pre_num*10 + i
            for j in range(2, number//2):
                if number % j == 0:
                    isP = False
                    break
            if isP:
                DFS(number)

    for i in first:
        DFS(i)


if __name__ == "__main__":
    solution()
