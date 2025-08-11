# https://codeforces.com/problemset/problem/1842/B
import math
T = int(input())
for _ in range(T):
    n,x = list(map(int, input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    not_x=~x
    tot_or=0
    not_poss=tot_or!=x
    i=0
    while i<n and a[i]&not_x==0 and not_poss:
        tot_or|=a[i]
        if tot_or==x: not_poss=False
        i+=1
    i=0
    while i<n and b[i]&not_x==0 and not_poss:
        tot_or|=b[i]
        if tot_or==x: not_poss=False
        i+=1
    i=0
    while i<n and c[i]&not_x==0 and not_poss:
        tot_or|=c[i]
        if tot_or==x: not_poss=False
        i+=1
    print("No") if not_poss else print("Yes")