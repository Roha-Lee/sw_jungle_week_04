import sys 
def find_smallest_jump_step(destination, small_rocks):
    max_speed = int((2*destination)**0.5 + 1)
    DP = [[float('inf')] * (max_speed + 1) for _ in range(destination+1)]
    DP[1][0] = 0

    for location in range(2, destination+1):
        if location in small_rocks:
            continue

        curr_max_speed = int((2*location)**0.5 + 1)    
        for speed in range(1, curr_max_speed):
            DP[location][speed] = min(
                DP[location-speed][speed-1] + 1,
                DP[location-speed][speed] + 1,
                DP[location-speed][speed+1] + 1)
    
    result = min(DP[destination])
    if result == float('inf'):
        return -1 
    return result
    
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