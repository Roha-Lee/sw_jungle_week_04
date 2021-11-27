from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
    arr.sort()

    checked = []
    for i in range(N):
        first, second = arr[i]
        if second <= arr[0][1]:
            checked.append((second, first))

    cnt = 0
    checked.sort()
    for j in checked:
        if j[1] <= checked[0][1]:
            cnt += 1
        
    print(cnt)