from sys import stdin

N = int(stdin.readline())
COST = [list(map(int, stdin.readline().split())) for _ in range(N)]

VISITED_ALL = (1 << N)-1
cache = [[None]*(1 << N) for _ in range(N)]

def dfs(last, visited):

    if visited == VISITED_ALL:
        print('last= ',last, 'visited= ', bin(visited), 'return= ',COST[last][0] or float('inf'))
        return COST[last][0] or float('inf')

    if cache[last][visited] is not None:
        print('last= ',last, 'visited= ', bin(visited), 'returnCache= ',cache[last][visited])
        return cache[last][visited]

    tmp = float('inf')
    for city in range(N):
        if not visited & (1 << city) and COST[last][city]:
            tmp = min(tmp, dfs(city, visited | (1 << city)) + COST[last][city])
    cache[last][visited] = tmp
    print('last= ',last, 'visited= ', bin(visited), 'cache= ',cache[last][visited])
    return tmp

print(dfs(0, 1))
print(cache)