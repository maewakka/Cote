import sys
from collections import deque

def solution():
    n = int(sys.stdin.readline())

    queue = deque()
    size = 0
    answer = []

    for _ in range(n):
        orders = sys.stdin.readline().split()
        order = orders[0]

        if order == 'push':
            queue.append(int(orders[1]))
            size += 1
        elif order == 'pop':
            if queue:
                answer.append(queue.popleft())
                size -= 1
            else:
                answer.append(-1)
        elif order == 'size':
            answer.append(size)
        elif order == 'empty':
            if queue:
                answer.append(0)
            else:
                answer.append(1)
        elif order == 'front':
            if queue:
                answer.append(queue[0])
            else:
                answer.append(-1)
        elif order == 'back':
            if queue:
                answer.append(queue[-1])
            else:
                answer.append(-1)


    for a in answer:
        print(a)
        
if __name__ == "__main__":
    solution()