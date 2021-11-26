import sys 
def find_smallest_jump_step(destination, small_rocks):
    max_speed = int((2*destination)**0.5 + 1)
    DP = [[float('inf')] * (max_speed + 1) for _ in range(destination+1)]
    DP[1][1] = 0

    for location in range(2, destination+1):
        if location in small_rocks:
            continue

        for speed in range(1, max_speed):
            if location - speed + 1 <= 0:
                break

            for prev_speed in [speed-1, speed, speed+1]:
                if  location > prev_speed:
                    DP[location][speed] = min(
                        DP[location][speed], 
                        DP[location-prev_speed][prev_speed] + 1)   
    
    return min(DP[destination])
    
if __name__ == '__main__':
    input = sys.stdin.readline
    destination, small_num = map(int, input().split())
    small_rocks = set([int(input()) for _ in range(small_num)])
    print(find_smallest_jump_step(destination, small_rocks))
'''
8 2 
3
6
'''