# https://codeforces.com/problemset/problem/1807/D
T = int(input())
for _ in range(T):
    n,q = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    prefix_sum = [0]*(n+1)
    for i in range(1,n+1):
        prefix_sum[i]=a[i-1]+prefix_sum[i-1]
    while q>0:
        l,r,k = [int(i) for i in input().split()]
        total = prefix_sum[l-1]+ prefix_sum[n]-prefix_sum[r] + (r-l+1)*k
        if total&1:
            print("YES")
        else:
            print("NO")
        q-=1

