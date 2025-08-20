# https://codeforces.com/problemset/problem/1914/D
import heapq
from typing import List, Tuple

def top3_max_with_indices(arr: List[int]) -> List[Tuple[int, int]]:
    
    min_heap: List[Tuple[int, int]] = []
    
    for i, val in enumerate(arr):
        heapq.heappush(min_heap, (val, i))
        if len(min_heap) > 3:
            heapq.heappop(min_heap)
    
    result = sorted(min_heap, key=lambda x: x[0], reverse=True)
    return result

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    res_a=top3_max_with_indices(a)
    res_b=top3_max_with_indices(b)
    res_c=top3_max_with_indices(c)
    res=a[0]+b[1]+c[2]
    for val1 in res_a:
        for val2 in res_b:
            for val3 in res_c:
                if val1[1]!=val2[1] and val2[1]!=val3[1] and val3[1]!=val1[1]:
                    res=max(res,val1[0]+val2[0]+val3[0])
    print(res)