import heapq
import sys
from collections import deque
from queue import PriorityQueue
import heapq
sys.setrecursionlimit(10 ** 7)

def solution():
    N, M = map(int, sys.stdin.readline().strip().split(' '))
    maze = [[] for i in range(N)]
    visited = [[False for i in range(M)] for i in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    deep = [[0 for i in range(M)] for i in range(N)]
    bfs_deque = deque()


    for i in range(N):
        line = sys.stdin.readline()
        for j in range(M):
            maze[i].append(int(line[j]))

    def Bfs(root):
        bfs_deque.appendleft((root[0], root[1]))

        while bfs_deque:
            x, y = bfs_deque.pop()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and ny>=0 and ny<M:
                    if maze[nx][ny] == 1:
                        maze[nx][ny] = maze[x][y] + 1
                        # for i in range(N):
                        #     print(maze[i])
                        # print("######################")
                        bfs_deque.appendleft((nx, ny))


    Bfs((0, 0))
    print(maze[N-1][M-1])


if __name__ == "__main__":
    solution()
