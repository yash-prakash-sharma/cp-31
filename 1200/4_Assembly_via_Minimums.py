# https://codeforces.com/problemset/problem/1857/C
T = int(input())
for _ in range(T):
    n = int(input())
    b = list(map(int, input().split()))
    b.sort()
    res=[]
    sz,i=n-1,0
    while sz>0:
        res.append(b[i])
        i+=sz
        sz-=1
    res.append(b[i-1])
    print(*res)