from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    applicant = [list(map(int, stdin.readline().split())) for _ in range(N)]
    applicant.sort()
    
    cnt = 1
    cutline = applicant[0][1]
    for i in range(N):
        if cutline > applicant[i][1]:
            cnt += 1
            cutline = applicant[i][1]
    print(cnt)