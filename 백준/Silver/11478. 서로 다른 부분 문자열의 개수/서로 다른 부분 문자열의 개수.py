import sys

def solution():
    word = sys.stdin.readline().strip()
    result = {}

    for i in range(1, len(word)+1):
        for j in range(len(word)+1-i):
            result[word[j:j+i]] = True

    print(len(result.keys()))

if __name__ == "__main__":
    solution()