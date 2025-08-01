# https://codeforces.com/problemset/problem/1704/B
T = int(input())
for _ in range(T):
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    l=a[0]-x
    r=a[0]+x
    res=0
    for i in range(1,n):
        cur_l=a[i]-x
        cur_r=a[i]+x
        l=max(l,cur_l)
        r=min(r,cur_r)
        if r<l:
            res+=1
            l=cur_l
            r=cur_r
    print(res)