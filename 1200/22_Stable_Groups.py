# https://codeforces.com/problemset/problem/1539/C
n,k,x = list(map(int, input().split()))
a = list(map(int, input().split()))
res = []
a.sort()
for i in range(1,n):
    diff=a[i]-a[i-1]
    if diff>x:
        res.append(diff)
res.sort()
i,ans=0,len(res)+1
while i<len(res):
    val=(res[i]-1)//x
    if val>k:
        break
    else:
        k-=val
        ans-=1
    i+=1
print(ans)