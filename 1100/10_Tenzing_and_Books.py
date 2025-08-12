# https://codeforces.com/problemset/problem/1842/B
import math
T = int(input())
for _ in range(T):
    n,x = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(3)]
    tot=0
    for i in range(3):
        cur,j=0,0
        while j<n and (cur|a[i][j]|x)==x:
            cur|=a[i][j]
            tot|=a[i][j]
            j+=1
    print("Yes") if tot==x else print("No")