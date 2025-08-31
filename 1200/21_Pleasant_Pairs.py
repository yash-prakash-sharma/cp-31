# https://codeforces.com/problemset/problem/1541/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    m = [-1]*(2*n+1)
    for i in range(n):
        m[a[i]]=i+1
    res=0
    # Approach 1
    # for val in range(3,2*n):
    #     i=1
    #     while i*i<=val:
    #         if m[i]!=-1 and val%i==0:
    #             j=val//i
    #             if i!=j and m[j]!=-1 and val==m[i]+m[j]:
    #                 res+=1
    #         i+=1
    a.sort()
    for i in range(n):
        for j in range(i+1,n):
            if a[i]*a[j] >= 2*n:
                break
            if a[i]*a[j]==m[a[i]]+m[a[j]]:
                res+=1
    print(res)