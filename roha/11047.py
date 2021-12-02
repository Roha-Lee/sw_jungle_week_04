import sys 
def find_min_coins(target_money, coins):
    coin_num = 0
    for coin in coins:
        num = target_money // coin
        coin_num += num
        target_money -= coin * num
    return coin_num

if __name__ == '__main__':
    input = sys.stdin.readline
    num_coin, target_money = map(int, input().split())
    coins = [int(input()) for _ in range(num_coin)]
    coins.reverse()
    print(find_min_coins(target_money, coins))