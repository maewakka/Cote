import sys
from collections import deque

def solution():
    case = int(sys.stdin.readline())
    answer = []

    for _ in range(case):
        n, m = map(int, sys.stdin.readline().split())
        queue = deque(list(map(int, sys.stdin.readline().split())))
        index = deque([i for i in range(n)])
        result = []

        while queue:
            if queue[0] != max(queue):
                queue.append(queue.popleft())
                index.append(index.popleft())
            else:
                result.append([queue.popleft(), index.popleft()])

            # print(queue, index)

        # print(result)

        for i in range(len(result)):
            if result[i][1] == m:
                answer.append(i+1)

    for a in answer:
        print(a)


if __name__ == "__main__":
    solution()