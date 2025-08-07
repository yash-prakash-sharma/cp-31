# https://codeforces.com/problemset/problem/1914/C
T = int(input())
for _ in range(T):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res,sum,maxi=0,0,0
    till=min(n,k)
    for i in range(till):
        maxi=max(maxi,b[i])
        sum+=a[i]
        res=max(res, sum+(k-i-1)*maxi)
    print(res)