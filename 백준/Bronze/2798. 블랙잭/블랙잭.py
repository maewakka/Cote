import sys
import itertools

def main():
    N, max_sum = map(int, sys.stdin.readline().split(' '))
    card_list = list(map(int, sys.stdin.readline().split(' ')))

    min_distance = 3000001
    answer = []

    for comb in itertools.combinations(card_list, 3):
        if sum(comb) <= max_sum and max_sum - sum(comb) <= min_distance:
            min_distance = max_sum - sum(comb)
            answer = comb

    print(sum(answer))


if __name__ == "__main__":
    main()