# https://codeforces.com/problemset/problem/1704/C
T = int(input())
for _ in range(T):
    n,m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    res=[]
    if (a[0]-1)+(n-a[m-1])>0:
        res.append((a[0]-1)+(n-a[m-1]))
    for i in range(1,m):
        if a[i]-a[i-1]-1>0:
            res.append(a[i]-a[i-1]-1)
    res.sort(reverse=True)
    days,safe=0,0
    for x in res:
        if x-2*days-1>=0:
            safe+=max(1,x-2*days-1)
        else:
            break
        days+=2
    print(n-safe)