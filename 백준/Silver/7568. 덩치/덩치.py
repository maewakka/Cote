import sys

def main():
    N = int(sys.stdin.readline())
    person = []

    for i in range(N):
        x, y = map(int, sys.stdin.readline().split())
        person.append([x, y])

    better_than = []

    for i in range(N):
        better = 0
        for j in range(N):
            if person[i][0] < person[j][0] and person[i][1] < person[j][1]:

                better += 1
        better_than.append(better)

    answer = [1 for i in range(len(better_than))]

    for i in range(len(better_than)):
        if i in better_than:
            same_count = better_than.count(i)
            index = 0
            for j in range(same_count):
                answer[better_than.index(i, index)] = i + 1
                index = better_than.index(i, index) + 1

    print(*answer)


if __name__ == "__main__":
    main()