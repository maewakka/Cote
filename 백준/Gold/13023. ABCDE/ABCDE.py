import heapq
import sys
from collections import deque
from queue import PriorityQueue
import heapq
sys.setrecursionlimit(10 ** 7)

def solution():
    N, M = map(int, sys.stdin.readline().strip().split(' '))

    friends = {}
    visited = [False for i in range(N)]
    result = False
    answer = 0
    dep = 1

    for i in range(N):
        friends[i] = []

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split(' '))

        friends[a].append(b)
        friends[b].append(a)

    def DFS(node, depth):
        if depth == 5:
            nonlocal result
            result = True
            return

        depth += 1
        visited[node] = True

        for i in friends[node]:
            if not visited[i]:
                DFS(i, depth)
        
        visited[node] = False

    for i in range(N):
        DFS(i, dep)
        if result:
            answer = 1
            break

    print(answer)


if __name__ == "__main__":
    solution()
