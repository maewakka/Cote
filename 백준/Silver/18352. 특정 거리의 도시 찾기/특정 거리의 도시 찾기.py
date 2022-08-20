import sys
from collections import deque

def solution():
    N, M, K, X = map(int, sys.stdin.readline().strip().split(' '))
    nodes = {}
    city_distance = [0 for i in range(N+1)]
    visited = [False for i in range(N+1)]
    queue = deque()

    for i in range(M):
        line = list(map(int, sys.stdin.readline().strip().split(' ')))
        a = line[0]
        b = line[1]

        if not a in nodes:
            nodes[a] = []
        nodes[a].append(b)

    queue.appendleft(X)
    visited[X] = True

    while queue:
        this_node = queue.pop()

        if this_node in nodes:
            for node in nodes[this_node]:
                if not visited[node]:
                    visited[node] = True
                    queue.appendleft(node)
                    city_distance[node] += city_distance[this_node] + 1

    if not K in city_distance:
        print(-1)
    else:
        for i in range(N+1):
            if city_distance[i] == K:
                print(i)


if __name__ == "__main__":
    solution()