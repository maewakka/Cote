import sys

def solution():
    N = int(sys.stdin.readline().strip())
    plus_numbers = []
    minus_numbers = []
    zero_count = 0
    one_count = 0
    answer = 0

    for i in range(N):
        number = int(sys.stdin.readline().strip())
        if number == 0:
            zero_count += 1
        elif number == 1:
            one_count += 1
        elif number > 1:
            plus_numbers.append(number)
        elif number < 0:
            minus_numbers.append(number)

    plus_numbers = sorted(plus_numbers)
    minus_numbers = sorted(minus_numbers, reverse=True)

    while len(plus_numbers) >= 2:
        data1 = plus_numbers.pop()
        data2 = plus_numbers.pop()
        answer += (data1 * data2)

    if len(plus_numbers) > 0:
        answer += plus_numbers.pop()

    while len(minus_numbers) >= 2:
        data1 = minus_numbers.pop()
        data2 = minus_numbers.pop()
        answer += (data1 * data2)

    if len(minus_numbers) > 0:
        if zero_count == 0:
            answer += minus_numbers.pop()

    if one_count != 0:
        answer += one_count

    print(answer)

if __name__ == "__main__":
    solution()

