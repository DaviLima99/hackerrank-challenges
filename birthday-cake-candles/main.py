import os


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthday_cake_candles(candles):
    max_candle = 0
    for candle in candles:
        max_candle = candle if candle > max_candle else max_candle

    return candles.count(max_candle)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # candles_count = int(input().strip())
    #
    # candles = list(map(int, input().rstrip().split()))

    candles = [3, 2, 1, 3]
    result = birthday_cake_candles(candles)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
