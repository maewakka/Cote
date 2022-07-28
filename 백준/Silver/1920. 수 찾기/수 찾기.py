import heapq
import sys
from collections import deque
from queue import PriorityQueue
import heapq
sys.setrecursionlimit(10 ** 7)

def solution():
    N = int(sys.stdin.readline().strip())
    array = list(map(int, sys.stdin.readline().strip().split(" ")))
    M = int(sys.stdin.readline().strip())
    find_list = list(map(int, sys.stdin.readline().strip().split(" ")))

    array.sort()

    for i in find_list:
        start = 0
        end = len(array)-1

        while True:
            middle = (start + end) // 2

            if i == array[middle]:
                print(1)
                break

            if start > middle:
                print(0)
                break

            if array[middle] >= i:
                end = middle-1
            else:
                start = middle+1








if __name__ == "__main__":
    solution()
