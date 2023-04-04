import sys

def solution():
    n = int(sys.stdin.readline())
    inputs = list(map(int, sys.stdin.readline().split()))
    inputs_set = list(set(inputs))
    result = []
    counts = {}

    inputs_set.sort()

    for i in range(len(inputs_set)):
        counts[inputs_set[i]] = i

    for input in inputs:
        result.append(counts[input])

    print(' '.join(list(map(str, result))))


if __name__ == "__main__":
    solution()