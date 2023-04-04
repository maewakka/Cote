import sys

def solution():
    n, m = map(int, sys.stdin.readline().split())
    monster_name = {}
    monster_num = {}
    answer = []

    for i in range(1, n+1):
        monster = sys.stdin.readline().strip()
        monster_name[monster] = i
        monster_num[i] = monster

    for _ in range(m):
        input = sys.stdin.readline().strip()

        if input.isdigit():
            answer.append(monster_num[int(input)])
        else:
            answer.append(monster_name[input])

    for a in answer:
        print(a)

if __name__ == "__main__":
    solution()