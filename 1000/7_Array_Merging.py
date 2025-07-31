# https://codeforces.com/problemset/problem/1831/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    i,j=1,1
    mp={}
    res=1
    prev=0
    while i<=n:
        if i==n or a[i]!=a[i-1]:
            length=i-prev
            mp[a[i-1]]=max(length,mp.get(a[i-1], 0))
            res=max(res,length)
            prev=i
        i+=1
    prev=0
    while j<=n:
        if j==n or b[j]!=b[j-1]:
            length=j-prev
            length=max(length,length+mp.get(b[j-1], 0))
            res=max(res,length)
            prev=j
        j+=1
    print(res)