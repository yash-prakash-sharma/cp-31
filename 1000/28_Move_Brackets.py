# https://codeforces.com/problemset/problem/1374/C
T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    bal=0
    res=0
    for c in s:
        if c=='(':
            bal+=1
        else:
            bal-=1
        if bal<0:
            res=max(res,abs(bal))
    print(res)