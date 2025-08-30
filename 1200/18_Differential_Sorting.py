# https://codeforces.com/problemset/problem/1635/C
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    flag=a[n-2]<=a[n-1]
    i=n-2
    while flag and i>=0:
        if a[i]>a[i+1]:
            if a[i+1]-a[n-1]>a[i+1]:
                flag=False
            else:
                a[i]=a[i+1]-a[n-1]
                res.append(i+2)
        i-=1     
    if flag:
        print(len(res))
        for x in res:
            print(x-1, x, n)
    else:
        print(-1)