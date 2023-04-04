import sys

def solution():
    n, m = map(int, sys.stdin.readline().split())
    words = {}
    answer = 0

    for _ in range(n):
        words[sys.stdin.readline().strip()] = True

    for _ in range(m):
        word = sys.stdin.readline().strip()
        if words.get(word) != None:
            answer += 1

    print(answer)

if __name__ == "__main__":
    solution()