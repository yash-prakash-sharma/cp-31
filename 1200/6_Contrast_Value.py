# https://codeforces.com/problemset/problem/1832/C
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    diff = []
    for i in range(1,n):
        if a[i]-a[i-1]!=0:
            diff.append(a[i]-a[i-1])
    if len(diff)==0:
        print(1)
    else:
        res=2
        for i in range(1,len(diff)):
            if (diff[i-1]<0 and diff[i]>0) or (diff[i-1]>0 and diff[i]<0):
                res+=1
        print(res)