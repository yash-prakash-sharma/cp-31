# https://codeforces.com/problemset/problem/1878/C
T = int(input())
for _ in range(T):
    n,k,x = [int(i) for i in input().split()]
    lower_limit=(k*(k+1))>>1
    upper_limit=((n*(n+1))>>1)-(((n-k)*(n-k+1))>>1)
    if x>=lower_limit and x<=upper_limit:
        print("YES")
    else:
        print("NO")