import heapq
import sys
from collections import deque
from queue import PriorityQueue
import heapq
sys.setrecursionlimit(10 ** 7)

def solution():
    N, M, V = map(int, sys.stdin.readline().strip().split(' '))

    node_list = {}
    visited = [False for i in range(N)]
    dfs_answer = []
    bfs_answer = []
    bfs_deque = deque()

    for i in range(N):
        node_list[i] = []

    for i in range(M):
        a, b = map(int, sys.stdin.readline().strip().split(' '))
        a-=1
        b-=1
        node_list[a].append(b)
        node_list[b].append(a)

    for i in range(N):
        node_list[i].sort()

    def DFS(node):
        if not node_list[node]:
            return

        visited[node] = True
        dfs_answer.append(node+1)

        for i in node_list[node]:
            if not visited[i]:
                DFS(i)

    def BFS(node):
        if not node_list[node]:
            return

        visited[node] = True
        bfs_answer.append(node+1)

        for i in node_list[node]:
            if not visited[i] and not (i in bfs_deque):
                bfs_deque.appendleft(i)
        while bfs_deque:
            BFS(bfs_deque.pop())

    DFS(V-1)
    visited = [False for i in range(N)]
    BFS(V-1)

    if not dfs_answer:
        dfs_answer.append(V)
    if not bfs_answer:
        bfs_answer.append(V)

    print(*dfs_answer)
    print(*bfs_answer)

if __name__ == "__main__":
    solution()
