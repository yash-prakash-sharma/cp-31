# https://codeforces.com/problemset/problem/1696/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    res=0
    prev=-1
    for i in range(n):
        if a[i]==0:
            if i-prev>1:
                res+=1
            prev=i
    if a[n-1] !=0:
        res+=1
    # we can replace all number with w then in 1 operation make all 0
    print(min(res,2))