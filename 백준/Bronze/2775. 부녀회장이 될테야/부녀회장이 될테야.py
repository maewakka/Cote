import sys

def people_count(a, b):
    if a == 0:
        return b

    people = 0

    for i in range(1, b+1):
        people += people_count(a-1, i)

    return people

def solution():
    case = int(sys.stdin.readline())
    answer = []

    for _ in range(case):
        k = int(sys.stdin.readline())
        n = int(sys.stdin.readline())

        answer.append(people_count(k, n))
        
    for a in answer:
        print(a)


if __name__ == "__main__":
    solution()