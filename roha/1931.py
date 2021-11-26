import sys 

def find_max_conferences(conferences):
    conferences = sorted(conferences, key = lambda x:x[0])
    conferences = sorted(conferences, key = lambda x:x[1])
    count = 0 
    curr_end = None
    for start, end in conferences:
        if curr_end is None or start >= curr_end: 
            curr_end = end
            count += 1
    return count

    
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    conferences = []
    for _ in range(n):
        start_time, end_time = map(int, input().split())
        conferences.append((start_time, end_time))
    print(find_max_conferences(conferences))
    