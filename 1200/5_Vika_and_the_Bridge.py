# https://codeforces.com/problemset/problem/1848/B
T = int(input())
for _ in range(T):
    n,k = list(map(int, input().split()))
    c = list(map(int, input().split()))
    mat = [[] for _ in range(k+1)]
    for i in range(1,k+1):
        mat[i].append(0)
    for i in range(n):
        mat[c[i]].append(i+1)
    for i in range(1,k+1):
        mat[i].append(n+1)
    res=n-1
    # print(mat)
    for i in range(1,k+1):
        el1,el2=-1,-1
        for j in range(1,len(mat[i])):
            cur=mat[i][j]-mat[i][j-1]-1
            if cur>=el1:
                el2=el1
                el1=cur
            elif cur>=el2:
                el2=cur
        res=min(res,max(el2,el1//2))
    print(res)