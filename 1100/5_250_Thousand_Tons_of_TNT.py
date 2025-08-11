# https://codeforces.com/problemset/problem/1899/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    if n==1:
        print(0)
        continue
    prefix=[0]*(n+1)
    for i in range(n):
        prefix[i+1]=a[i]+prefix[i]
    k,res=1,0
    # TC= n + n/2 + n/3 + . . . + 1 =n(1 + 1/2 + ... + 1/n) = nlogn
    while k<=(n//2):
        maxi=0
        mini=float('inf')
        if n%k!=0:
            k+=1
            continue
        for i in range(1,n//k+1):
            sum=prefix[n-(i-1)*k]-prefix[n-(i)*k]
            maxi=max(sum,maxi)
            mini=min(sum,mini)
        res=max(res,maxi-mini)
        k+=1
    print(res)