import heapq
import sys
from collections import deque
from queue import PriorityQueue
import heapq



def solution():
    N, M = map(int, sys.stdin.readline().strip().split(" "))
    sys.setrecursionlimit(10 ** 7)

    connected = {}
    visited = [False for _ in range(N)]
    answer = 0

    for i in range(N):
        connected[i] = []

    for _ in range(M):
        A, B = map(int, sys.stdin.readline().strip().split(" "))
        A -= 1
        B -= 1
        connected[A].append(B)
        connected[B].append(A)

    def DFS(visit_node):
        if visited[visit_node]:
            return
        visited[visit_node] = True
        for i in connected[visit_node]:
            DFS(i)

    for i in range(N):
        if not visited[i]:
            DFS(i)
            answer+=1

    print(answer)

if __name__ == "__main__":
    solution()
