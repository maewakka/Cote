import sys

def solution():
    n, m = map(int, sys.stdin.readline().split())

    no_listen = {}
    answer = []

    for _ in range(n):
        name = sys.stdin.readline().strip()
        no_listen[name] = True

    for _ in range(m):
        name = sys.stdin.readline().strip()
        if no_listen.get(name) != None:
            answer.append(name)

    answer.sort()
    print(len(answer))
    for name in answer:
        print(name)



if __name__ == "__main__":
    solution()