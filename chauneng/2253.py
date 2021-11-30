from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
SMALL = set([int(stdin.readline()) for _ in range(M)])
check = [[] for _ in range(N + 1)]
dx = (-1, 0, 1)
queue = deque()
queue.append([0, 1, 0])
ans = -1
while queue:
    speed, position, jump = queue.popleft()
    for i in range(3):
        newSpeed = speed + dx[i]
        if newSpeed <= 0:
            continue
        new_pos = position + newSpeed
        if new_pos == N:
            ans = jump + 1 
            print(ans)
            exit(0)
            
        if new_pos not in SMALL and new_pos < N and newSpeed not in check[new_pos]: 
            check[new_pos].append(newSpeed)
            queue.append([newSpeed, new_pos, jump+1])

print(ans)