# https://codeforces.com/problemset/problem/1543/A
import math
T = int(input())
for _ in range(T):
    a,b = list(map(int, input().split()))
    if a==b:
        print(0, 0)
    else:
        val=abs(a-b)
        print(val, min(a%val,val-(a%val)))