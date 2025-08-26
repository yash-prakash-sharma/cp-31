# https://codeforces.com/problemset/problem/1790/D
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    m={}
    res=0
    for x in sorted(a):
        m[x]=m.get(x,0)+1
    for key in m:
        res+=max(m.get(key)-m.get(key-1,0),0)
    print(res)