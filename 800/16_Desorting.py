# https://codeforces.com/problemset/problem/1853/A
T = int(input())
for cnt in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    mini=1000000000
    sorted=True
    for i in range(1,n):
        if a[i]<a[i-1]:
            sorted=False
            break
        # operations required to make array un sorted
        req_ops=(a[i]-a[i-1]+2)//2
        if mini>req_ops:
            mini=req_ops
    if sorted:
        print(mini)
    else:
        print(0)