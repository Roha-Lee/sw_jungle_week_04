import sys 
from collections import defaultdict

def RabinKarp(word1, word2, window_size):
    q = 1<<31 - 1
    m = 100
    hash_val = 0
    constant = m ** window_size
    word1_dict = defaultdict(list)

    for i in range(window_size):
        hash_val *= m
        hash_val += ord(word1[i]) - ord('a')
        hash_val %= q
    word1_dict[hash_val].append(0)
    
    for start_pos in range(1, len(word1)-window_size+1):
        hash_val *= m
        hash_val -= (ord(word1[start_pos-1]) - ord('a')) * constant
        hash_val += ord(word1[start_pos+window_size-1]) - ord('a')
        hash_val %= q
        word1_dict[hash_val].append(start_pos)
    
    hash_val = 0
    for i in range(window_size):
        hash_val *= m
        hash_val += ord(word2[i]) - ord('a')
        hash_val %= q
    
    if hash_val in word1_dict:
        word2_str = word2[:window_size]
        for i in word1_dict[hash_val]:
            word1_str = word1[i:i+window_size]
            if word1_str == word2_str:
                return word2_str

    for start_pos in range(1, len(word2)-window_size+1):
        
        hash_val *= m
        hash_val -= (ord(word2[start_pos-1]) - ord('a')) * constant
        hash_val += ord(word2[start_pos+window_size-1]) - ord('a')
        hash_val %= q
        if hash_val in word1_dict:
            word2_str = word2[start_pos:start_pos + window_size]
            for i in word1_dict[hash_val]:
                word1_str = word1[i:i+window_size]
                if word1_str == word2_str:
                    return word2_str
        
def find_longest_common_substring(word1, word2):
    left = 1
    right = min(len(word1), len(word2))
    best_substring = ''
    while left <= right:
        mid = (left + right) // 2
        substring = RabinKarp(word1, word2, mid)
        if substring:
            left = mid + 1
            best_substring = substring
        else:
            right = mid - 1
    return len(best_substring), best_substring


if __name__ == '__main__':
    input = sys.stdin.readline
    word1 = input().rstrip()
    word2 = input().rstrip()
    print(*find_longest_common_substring(word1, word2), sep='\n')


