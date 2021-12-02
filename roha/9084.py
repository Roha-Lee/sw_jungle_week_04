import sys
def count_method_of_target_money(coins, target_money):
    DP = [[0] * (target_money + 1) for _ in range(len(coins) + 1)]
    for money in range(1, target_money + 1):
        DP[0][money] = 0
    for i in range(len(coins)+1):
        DP[i][0] = 1
    for money in range(1, target_money + 1):
        for idx, coin in enumerate(coins, 1):
            DP[idx][money] = DP[idx-1][money]
            if money >= coin:
                DP[idx][money] += DP[idx][money - coin]
    return DP[-1][-1]    

if __name__ == '__main__':
    input = sys.stdin.readline
    testcase = int(input())
    for _ in range(testcase):
        num_coin = int(input())
        coins = list(map(int, input().split()))
        target_money = int(input())
        print(count_method_of_target_money(coins, target_money))