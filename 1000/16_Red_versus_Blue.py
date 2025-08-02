# https://codeforces.com/problemset/problem/1659/A
T = int(input())
for _ in range(T):
    n,r,b = list(map(int, input().split()))
    res=""
    consq_red=r//(b+1)
    residual_red=r%(b+1)
    for i in range(b+1):
        res+='R'*consq_red
        if residual_red>0:
            res+='R'
            residual_red-=1
        if i!=b:
            res+='B'
    print(res)