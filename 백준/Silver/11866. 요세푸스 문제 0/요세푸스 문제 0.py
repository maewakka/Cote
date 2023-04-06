import sys

def solution():
    n, k = map(int, sys.stdin.readline().split())

    queue = [i for i in range(1, n+1)]
    result = []
    index = 0

    while queue:
        index = (index + k - 1) % len(queue)
        result.append(queue[index])
        del queue[index]

    answer = '<' + ', '.join(list(map(str, result))) +'>'
    print(answer)

if __name__ == "__main__":
    solution()