# https://codeforces.com/problemset/problem/1840/C
T = int(input())
for _ in range(T):
    n,k,q = list(map(int,input().split()))
    a = list(map(int,input().split()))
    res,i,prev=0,0,-1
    while i<=n:
        if i==n or a[i]>q:
            length = i-prev
            length -= k
            if length>0:
                res+=(length*(length+1))//2
            prev=i
        i+=1

    print(res)