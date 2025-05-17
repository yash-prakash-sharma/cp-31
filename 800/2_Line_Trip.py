#https://codeforces.com/problemset/problem/1901/A
T = int(input())
for cnt in range(T):
    n,x = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    res=a[0]
    # find max distance in between stations
    for i in range(1,n):
        res=max(res,a[i]-a[i-1])
    # since from last station we need to go and come back from point x
    res=max(res,2*(x-a[n-1]))
    print(res)