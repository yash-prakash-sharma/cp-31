# https://codeforces.com/problemset/problem/1691/B
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    res = [0]*(n+1)
    poss=True
    i=0
    while poss and i < n:
        l,r=i,i
        # find range with same size
        while r<n-1 and a[r+1]==a[l]:
            r+=1
        # exit if not possible
        if r-l+1==1:
            poss=False
            break
        # update result
        res[l+1]=r+1
        for j in range(l+2,r+2): res[j]=j-1
        i=r+1
        
    if poss:
        for i in range(1,n+1):
            print(res[i], end=' ')
        print()
    else:
        print(-1)