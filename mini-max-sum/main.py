#!/bin/python3
#
# Complete the 'miniMaxSum' function below.

# The function accepts INTEGER_ARRAY arr as parameter.
#

def mini_max_sum(param):
    max_sum = 0
    min_sum = 0

    for index in range(0, len(param)):
        min_index = index

        for right in range(index + 1, len(param)):
            if param[right] < param[min_index]:
                min_index = right

        param[index], param[min_index] = param[min_index], param[index]

    for index, item in enumerate(param):
        print(f"{index} -> {item}")
        max_sum = max_sum if index < 1 else max_sum + item
        min_sum = min_sum if index == len(param) - 1 else min_sum + item

    print(f'{min_sum} {max_sum}')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    mini_max_sum(arr)
