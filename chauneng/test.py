from sys import stdin

dp = [0, 1]

N = int(stdin.readline())

def fibonacci() -> int:

    n = 0
    tmp = int()

    while n < N:
        n += 1
        tmp = ((dp[0] % 15746) + (dp[1] % 15746)) %15746
        if n % 2:
            dp[0] = tmp
        else:
            dp[1] = tmp
    
    return tmp

print(fibonacci())
