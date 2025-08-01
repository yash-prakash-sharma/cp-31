# https://codeforces.com/problemset/problem/1715/B
T = int(input())
for _ in range(T):
    n,k,b,s = list(map(int, input().split()))
    lower=b*k
    upper=n*(k-1) + lower
    if s>=lower and s<=upper:
        val=k-1
        print(min(lower+val,s), end=' ')
        s-=min(lower+val,s)
        for i in range(n-1):
            val=min(val,s)
            print(val, end=' ')
            s-=val
        print()
    else:
        print(-1)