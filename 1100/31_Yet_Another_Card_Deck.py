# https://codeforces.com/problemset/problem/1511/C
n,q = list(map(int, input().split()))
a = list(map(int, input().split()))
t = list(map(int, input().split()))
res = []
occ = [0]*51
for i in range(n-1,-1,-1):
    occ[a[i]]=i+1
for x in t:
    res.append(occ[x])
    for j in range(1,51):
            if occ[j]<occ[x]:
                occ[j]+=1
    occ[x]=1
print(*res)