import sys
from collections import deque

def solution():
    text = deque(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline())

    cursor = len(text)
    left_string = text
    right_string = deque([])

    for i in range(0, N):
        command = sys.stdin.readline().strip().split(' ')

        if command[0] == 'L' and left_string:
            right_string.appendleft(left_string.pop())
        elif command[0] == 'D' and right_string:
            left_string.append(right_string.popleft())
        elif command[0] == 'B' and left_string:
            left_string.pop()
        elif command[0] == 'P':
            left_string.append(command[1])

    result = left_string + right_string

    print("".join(result))



if __name__ == "__main__":
    solution()