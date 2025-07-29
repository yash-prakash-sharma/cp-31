# https://codeforces.com/problemset/problem/1883/C
T = int(input())
for _ in range(T):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    res=k
    ev_cnt=0
    for x in a:
        if x%k==0:
            res=0
            break
        elif x%2==0:
            ev_cnt+=1
        res=min(res, k-(x%k))
    if k==4:
        if ev_cnt>=2:
            res=0
        elif ev_cnt==1:
            res=min(res,1)
        else:
            res=min(res,2)
    print(res)