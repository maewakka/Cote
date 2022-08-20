import sys
from collections import deque

def solution():
    N, M = map(int, sys.stdin.readline().strip().split(' '))
    nodes = {}


    for i in range(M):
        line = list(map(int, sys.stdin.readline().strip().split(' ')))
        a = line[0]
        b = line[1]

        if not b in nodes:
            nodes[b] = []
        nodes[b].append(a)

    def BFS(root):
        visited = [False for i in range(N + 1)]
        result = 0
        queue = deque()

        queue.appendleft(root)
        visited[root] = True

        while queue:
            this_node = queue.pop()

            if this_node in nodes:
                for node in nodes[this_node]:
                    if not visited[node]:
                        visited[node] = True
                        queue.appendleft(node)
                        result += 1

        return result

    temp = [0 for i in range(N+1)]
    answer = []

    for i in range(1, N+1):
        temp[i] = BFS(i)

    max_val = max(temp)
    max_val_count = temp.count(max_val)

    for i in range(max_val_count):
        answer.append(temp.index(max_val))
        temp[temp.index(max_val)] = 0

    print(*answer)

if __name__ == "__main__":
    solution()