from sys import path, stdin

cities = int(stdin.readline())
fare = [list(map(int, stdin.readline().split())) for _ in range(cities)]

def dfs(start: int,departure: int, part_sum: int) -> None:
    global ans
    if part_sum > ans:
        return 
    if sum(visited) == cities:
        if fare[departure][start]:
            part_sum += fare[departure][start]
            ans = min(ans, part_sum)
            return 
    
    for arrive in range(cities):
        if not visited[arrive]:
            if not fare[departure][arrive]:
                return 
            else:
                visited[arrive] = 1
                dfs(start, arrive, part_sum + fare[departure][arrive])
                visited[arrive] = 0



    # # tmp = 0
    # for arrive in range(cities):
    #     if not visited[arrive]:
    #         # visited[arrive] = 1            
    #         if not fare[departure][arrive]:
    #             tmp = float('inf')
    #             return
    #         else:
    #             tmp = tmp + fare[departure][arrive]
    #             tmp += fare[departure][arrive]
    #             if sum(visited) == cities:
    #                 if fare[arrive][start]:
    #                     tmp += fare[arrive][start]
    #                 else:
    #                     tmp = float('inf')
    #             else:
    #                 visited[arrive] = 1
    #                 dfs(start, arrive)
    #                 visited[arrive] = 0

ans = float('inf')
visited = [0] * cities
for i in range(cities):
    visited[i] = 1
    # tmp = 0
    dfs(i, i, 0)
    visited[i] = 0
    # ans = min(ans, tmp)

print(ans)