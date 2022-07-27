import sys

def solution():
    text = sys.stdin.readline().strip()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = [0 for i in range(len(alphabet))]

    for char in text:
        result[alphabet.find(char)] += 1

    print(*result)


if __name__ == "__main__":
    solution()