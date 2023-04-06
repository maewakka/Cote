import sys

def solution():
    n = int(sys.stdin.readline())
    answer = []

    stack = []
    size = 0
    for _ in range(n):
        orders = sys.stdin.readline().split()

        if orders[0] == 'push':
            num = int(orders[1])
            stack.append(num)
            size += 1
        elif orders[0] == 'top':
            if stack:
                answer.append(stack[-1])
            else:
                answer.append(-1)
        elif orders[0] == 'size':
            answer.append(size)
        elif orders[0] == 'empty':
            if stack:
                answer.append(0)
            else:
                answer.append(1)
        elif orders[0] == 'pop':
            if stack:
                answer.append(stack.pop())
                size -= 1
            else:
                answer.append(-1)

    for a in answer:
        print(a)

if __name__ == "__main__":
    solution()