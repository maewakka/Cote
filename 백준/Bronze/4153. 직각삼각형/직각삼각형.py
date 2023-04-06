import sys

def solution():
    answer = []

    while True:
        nums = list(map(int, sys.stdin.readline().split()))
        if sum(nums) == 0:
            break

        nums.sort()

        if nums[0]**2 + nums[1]**2 == nums[2]**2:
            answer.append("right")
        else:
            answer.append("wrong")

    for a in answer:
        print(a)

if __name__ == "__main__":
    solution()