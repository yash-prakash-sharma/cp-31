# https://codeforces.com/problemset/problem/1665/B
# Gives TLE For CF
import sys
import math

T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    freq_map = {}
    max_freq = 0
    
    for num in a:
        freq_map[num] = freq_map.get(num, 0) + 1
        if freq_map[num] > max_freq:
            max_freq = freq_map[num]
    
    left_places=n-max_freq
    copy_ops=0 if left_places<=0 else math.ceil(math.log2(left_places/max_freq + 1))
    print(left_places + copy_ops)