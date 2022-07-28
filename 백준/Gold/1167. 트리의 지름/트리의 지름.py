import heapq
import sys
from collections import deque
from queue import PriorityQueue
import heapq
sys.setrecursionlimit(10 ** 7)

def solution():
    N = int(sys.stdin.readline().strip())

    node_list = {}
    answer = 0

    for i in range(1, N+1):
        node_list[i] = []

    for i in range(N):
        command = list(map(int, sys.stdin.readline().strip().split(' ')))
        node_num = command[0]
        command = command[1:]
        command.remove(-1)

        for j in range(0, len(command), 2):
            node_list[node_num].append([command[j], command[j+1]])

    def BFS(root):
        weight = 0
        distance = [0 for i in range(N + 1)]
        bfs_deque = deque()
        visited = [False for i in range(N + 1)]

        bfs_deque.appendleft(root)

        while bfs_deque:
            node = bfs_deque.pop()
            visited[node] = True

            for i in range(len(node_list[node])):
                next_node = node_list[node][i][0]

                if not visited[next_node]:
                    weight = distance[node] + node_list[node][i][1]
                    distance[next_node] = weight
                    bfs_deque.appendleft(next_node)

        return distance

    first_result = BFS(1)
    max_node = first_result.index(max(first_result))

    print(max(BFS(max_node)))

if __name__ == "__main__":
    solution()
