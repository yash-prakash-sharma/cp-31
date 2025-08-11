# https://codeforces.com/problemset/problem/1873/E
# https://codeforces.com/problemset/problem/1891/B
T = int(input())
for _ in range(T):
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    l,r=1,2000000000
    while l<=r:
        res=(l+r)>>1
        cap=0
        for val in a: cap+=max(0,res-val)
        if cap<=x: l=res+1
        else: r=res-1
        # print(l, " ", r)
    print(r)