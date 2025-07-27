# https://codeforces.com/problemset/problem/1440/B
T = int(input())
for _ in range(T):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    res=0
    ind=len(a)
    sz=(n+2)//2
    while k>0:
        ind-=sz
        res+=a[ind]
        k-=1
    print(res)
