n=[sum(map(int,i.split('+')))for i in input().split('-')];print(n[0]-sum(n[1:]))