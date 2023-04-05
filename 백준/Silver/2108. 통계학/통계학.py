import sys

def solution():
    n = int(sys.stdin.readline())
    nums = []
    dict = {}

    for _ in range(n):
        num = int(sys.stdin.readline())
        if dict.get(num) == None:
            dict[num] = 0
        nums.append(num)
        dict[num] += 1

    nums.sort()

    print(round(sum(nums)/len(nums)))
    print(nums[len(nums)//2])

    result = list(dict.items())
    result_values = list(dict.values())
    result.sort(key=lambda x:(-x[1], x[0]))

    if result_values.count(max(result_values)) >= 2:
        print(result[1][0])
    else:
        print(result[0][0])


    print(nums[-1] - nums[0])


if __name__ == "__main__":
    solution()