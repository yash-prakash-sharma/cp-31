# https://codeforces.com/problemset/problem/1418/A
import math
T = int(input())
for _ in range(T):
    x,y,k = list(map(int, input().split()))
    # 1+(x-1)*a - y*24 = k
    # remember python floating point acc. issue
    res =((y*k + k +x-3)//(x-1))
    res+=k
    print(res)