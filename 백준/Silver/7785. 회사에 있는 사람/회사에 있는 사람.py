import sys

def solution():
    n = int(sys.stdin.readline())
    logs = {}

    for _ in range(n):
        name, status = sys.stdin.readline().split()

        if status == 'enter':
            logs[name] = True
        if status == 'leave':
            del logs[name]

    result = sorted(logs.keys(), reverse=True)

    for name in result:
        print(name)


if __name__ == "__main__":
    solution()