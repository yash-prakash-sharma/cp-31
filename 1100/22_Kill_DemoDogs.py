# https://codeforces.com/problemset/problem/1731/B
mod = 1000000007
T = int(input())
for _ in range(T):
    n = int(input())
    if n==1:
        res=1
    else:
        res = (((n*(n+1)*(2*n+1))//6)%mod + (((n-1)*n*(2*n-1))//6)%mod + ((n*(n-1))//2)%mod)%mod
    print((res*2022)%mod)