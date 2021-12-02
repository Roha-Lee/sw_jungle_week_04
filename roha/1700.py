import sys 
def minimum_switch(num_plugs, items):
    curr_items = []
    count = 0
    for idx, item in enumerate(items):
        if item not in curr_items and len(curr_items) < num_plugs:
            curr_items.append(item)
        elif item not in curr_items and len(curr_items) >= num_plugs:
            distances = {_item:float('inf') for _item in curr_items}
            for remain_idx in range(idx + 1, len(items)):
                if items[remain_idx] in curr_items and distances[items[remain_idx]] == float('inf'):
                    distances[items[remain_idx]] = remain_idx
            pop_item = sorted(distances.items(), key = lambda x: x[1])[-1][0]        
            curr_items.remove(pop_item)
            curr_items.append(item)
            count += 1
    return count 
    

if __name__ == '__main__':
    input = sys.stdin.readline
    num_plugs, max_items = map(int, input().split())
    items = list(map(int, input().split()))
    print(minimum_switch(num_plugs, items))