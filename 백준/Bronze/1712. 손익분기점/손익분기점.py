import sys

def main():
    fixed_cost, variable_cost, selling_cost = map(int, sys.stdin.readline().split())

    total_cost = fixed_cost
    total_sales = 0
    break_even_point = 1

    if variable_cost >= selling_cost:
        break_even_point = -1
    else:
        break_even_point = fixed_cost // (selling_cost - variable_cost) + 1

    print(break_even_point)

if __name__ == '__main__':
    main()